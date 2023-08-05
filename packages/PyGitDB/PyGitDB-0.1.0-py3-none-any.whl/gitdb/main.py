"""
Init and load GitDB
"""
import argparse
import os
from pathlib import Path
from time import perf_counter
from typing import Optional

from loguru import logger
from pydantic import SecretStr
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from gitdb.api.client import APIClient, APIClientConfig
from gitdb.loader import Loader


def init(
    repo: str,
    owner: str,
    path: str = "gitdb.db",
    clean: bool = False,
    token: Optional[SecretStr] = None,
) -> Session:
    """
    Initialize DuckDB with Git stats.
    """
    exec_start_time = perf_counter()
    logger.info(f"Starting GitDB in {path}...")

    api_client = APIClient(
        config=APIClientConfig(
            repo=repo,
            owner=owner,
            token=token,
        )
    )

    db_path = Path(path)
    if clean and db_path.exists():
        db_path.unlink()

    engine = create_engine(f"duckdb:///{path}")

    base_instance = declarative_base()
    session_maker = sessionmaker(
        autocommit=True, bind=engine, expire_on_commit=False, autoflush=False
    )
    with session_maker() as session:
        loader = Loader(client=api_client, session=session, base_instance=base_instance)
        loader.load()

        logger.info(
            f"Loaded all data in {(perf_counter() - exec_start_time) / 60} min."
        )
        return session


def cli():
    """
    Prep the CLI
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help="Repo to analyze", type=str)
    parser.add_argument("-o", "--owner", help="Repo owner", type=str)
    parser.add_argument(
        "-f", "--file", help="Db file path", type=str, default="gitdb.db"
    )
    parser.add_argument("--clean", help="Clean the existing db", action="store_true")

    args = parser.parse_args()

    init(
        repo=args.repo,
        owner=args.owner,
        path=args.file,
        clean=args.clean,
        token=os.getenv("GITHUB_API_TOKEN"),
    )
