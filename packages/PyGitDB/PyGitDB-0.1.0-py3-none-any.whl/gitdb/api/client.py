"""
Module containing helper utilities
to handle Github API calls
"""
import base64
import concurrent
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from loguru import logger
from pydantic import BaseModel, SecretStr

from gitdb.dao.models import QueryVariables

PER_PAGE = 100


class APIClientConfig(BaseModel):
    """
    Defines how to initialize the API Client
    """

    root: str = "api.github.com"  # We only support GitHub API
    owner: str = "open-metadata"
    repo: str = "OpenMetadata"
    token: Optional[SecretStr] = None
    start_date: str = "Aug 1 2021"  # Format `%b %d %Y`
    timeout: int = 60 * 5
    graphql: str = "graphql"


class APIClient:
    """
    Manage API requests to extract data
    """

    def __init__(self, config: APIClientConfig):
        self.config = config

        logger.info(f"Preparing client with {self.config}")

        self.root = Path(self.config.root)

        self._token = None
        self.start_date = datetime.strptime(
            getattr(self.config, "start_date", "Aug 1 2021"), "%b %d %Y"
        )

        self.auth_headers = (
            {"Authorization": f"token {self.token}"} if self.token else {}
        )

        # Only pass the token header if available in the config or as an env variable
        self.headers = {
            "Accept": "application/vnd.github.v3.star+json",
            **self.auth_headers,
        }

        self.repo_path = self.root / "repos" / self.config.owner / self.config.repo

    @property
    def token(self) -> str:
        """
        Retrieve API token
        """
        if not self._token:
            if self.config.token:
                self._token = self.config.token.get_secret_value()

            else:
                token = os.environ.get("API_TOKEN")
                if token is None:
                    logger.warning(
                        "No token set in the API config and no `API_TOKEN` env variable found."
                        " Please set it and rerun if you want to extract all the data."
                    )

                self._token = token

        return self._token

    @staticmethod
    def url(path: Path) -> str:
        """Return the HTTPS URL"""
        return "https://" + str(path)

    def post_query(
        self, query: str, variables: Optional[QueryVariables] = None
    ) -> Optional[Dict[str, Any]]:
        """Post graphql query to endpoint"""
        endpoint = self.url(self.config.root / Path(self.config.graphql))
        json_ = {
            "query": query,
            **({"variables": variables.dict()} if variables else {}),
        }

        res = requests.post(endpoint, json=json_, headers=self.auth_headers)
        if res.status_code == 200:
            return res.json()
        return None

    def _get(self, path: str, headers: Dict[str, str]):
        return requests.get(path, headers=headers, timeout=self.config.timeout)

    def get(self, path: Path):
        """
        Prepare an HTTPS URL from the given path
        """
        return self._get(self.url(path), headers=self.headers).json()

    def get_all_simple(self, path: Path, option: Optional[str] = None):
        """
        Run a simple request
        Args:
            path: path root to call
            option: any extra filters to be passed to the request
        """
        path_str = self.url(path)
        option_str = option if option else ""

        req = path_str + "?simple=yes&per_page=100&page=1" + option_str

        res = requests.get(req, headers=self.headers, timeout=self.config.timeout)
        data = res.json()
        while "next" in res.links.keys():
            res = requests.get(
                res.links["next"]["url"],
                headers=self.headers,
                timeout=self.config.timeout,
            )
            data.extend(res.json())

        return data

    def get_all_from_thread(
        self, request: str, pages: int, threads: int, partition: int
    ) -> List[dict]:
        """
        Function to be call from within a thread
        Args:
            request: path to call
            pages: number pages to retrieve
            threads: number of threads (partitions) that will be executed
            partition: specific partition to compute

        Returns: List with data of all pages
        """
        data = []

        pages_to_compute = [
            page for page in range(1, pages + 1) if page % threads == partition
        ]

        for page in pages_to_compute:
            res = requests.get(
                request.format(page=page),
                headers=self.headers,
                timeout=self.config.timeout,
            )
            data.extend(res.json())

        return data

    def get_all_parallel(
        self, path: Path, total: int, threads: int = 5, option: Optional[str] = None
    ):
        """
        Return all pages from a given request
        Args:
            path: path root to call
            total: total number of elements. We'll compute the pages accordingly
            threads: number of threads to spin
            option: any extra filters to be passed to the request
        """

        path_str = self.url(path)
        option_str = option if option else ""

        pages = total // PER_PAGE + 1

        # We'll format the page here
        request = path_str + "?simple=yes&per_page=100&page={page}" + option_str
        # We'll concat all the results from the ThreadPool
        data = []

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(
                    self.get_all_from_thread, request, pages, threads, partition
                )
                for partition in range(threads)
            ]

        for future in concurrent.futures.as_completed(futures):
            pages_data = future.result()
            data.extend(pages_data)

        return data

    def get_all_query_from_thread(
        self,
        query: str,
        search_query: str,
        partition: int,
        threads: int,
        cursors: List[Optional[str]],
    ) -> List[dict]:
        """
        Function to be called from within a thread for graphql query
        Args:
            query: query to run
            search_query: inner query filtering for search
            partition: partition being processed
            threads: number of threads being processed
            cursors: list of cursors to call

        Returns: List of data of all partitioned pages
        """

        data = []
        cursors_to_compute = [
            cursor for idx, cursor in enumerate(cursors) if idx % threads == partition
        ]

        for cursor in cursors_to_compute:
            variables = QueryVariables(
                first=PER_PAGE,
                after=cursor,
                search_query=search_query,
            )

            res = self.post_query(query=query, variables=variables)
            # This only works for our search queries of Issues and Pulls
            data_ = [elem["node"] for elem in res["data"]["search"]["edges"]]
            data.extend(data_)

        return data

    def get_all_search_query_parallel(
        self, query: str, search_query: str, total: int, threads: int = 5
    ) -> List[dict]:
        """
        Return all pages from a graphql query
        Args:
            query: graphql query to format with offset
            search_query: inner query filtering for search
            total: total elements to query
            threads: number of workers to spin up
        """

        data = []

        # Page 0 cursor is None, we'll add it later
        pages = range(1, total // PER_PAGE + 1)
        cursors: List[Optional[str]] = [
            base64.b64encode(f"cursor:{(page * PER_PAGE)}".encode("utf-8")).decode(
                "utf-8"
            )
            for page in pages
        ]
        # handle first cursor
        cursors.append(None)

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(
                    self.get_all_query_from_thread,
                    query,
                    search_query,
                    partition,
                    threads,
                    cursors,
                )
                for partition in range(1, threads + 1)
            ]

        for future in concurrent.futures.as_completed(futures):
            pages_data = future.result()
            data.extend(pages_data)

        return data
