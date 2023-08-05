"""
Module to load stats from the APIClient
to the database
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict

from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.contributors import ContributorsDAO
from gitdb.dao.issues import IssuesDAO
from gitdb.dao.models import Totals
from gitdb.dao.reviews import ReviewsDAO
from gitdb.dao.stars import StarsDAO
from gitdb.dao.weekly_commits import WeeklyCommitsDAO


class Loader:
    """
    Handles the relation between the client
    and the database
    """

    def __init__(
        self, client: APIClient, session: Session, base_instance: DeclarativeMeta
    ):
        self.client = client
        self.session = session
        self.totals = self.get_totals()

        self.models = [
            ReviewsDAO(
                client=client,
                session=self.session,
                base_instance=base_instance,
                totals=self.totals,
            ),
            IssuesDAO(
                client=client,
                session=self.session,
                base_instance=base_instance,
                totals=self.totals,
            ),
            StarsDAO(
                client=client,
                session=self.session,
                base_instance=base_instance,
                totals=self.totals,
            ),
            WeeklyCommitsDAO(
                client=client, session=self.session, base_instance=base_instance
            ),
            ContributorsDAO(
                client=client, session=self.session, base_instance=base_instance
            ),
        ]

        base_instance.metadata.create_all(bind=self.session.bind)

    def get_totals(self) -> Totals:
        """Get the total number of elements for pagination"""
        query = """
        {{
          repository(owner:"{owner}", name:"{repo}") {{
            issues {{
              totalCount
            }}
            pullRequests {{
              totalCount
            }}
            stargazerCount
          }}
        }}
        """.format(
            owner=self.client.config.owner,
            repo=self.client.config.repo,
        )
        res: Dict[str, Any] = self.client.post_query(query)
        data = res["data"]["repository"]

        return Totals(
            total_stars=data["stargazerCount"],
            total_issues=data["issues"]["totalCount"],
            total_pulls=data["pullRequests"]["totalCount"],
        )

    def load(self) -> None:
        """
        Run all models, load their data and store it
        """
        with ThreadPoolExecutor(max_workers=len(self.models)) as executor:
            futures = [executor.submit(model.process) for model in self.models]

        for future in as_completed(futures):
            # Run until done with all threads
            self.session.bulk_save_objects(future.result())
