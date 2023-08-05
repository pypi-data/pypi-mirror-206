"""
Handle stars data
"""
from typing import Any, Dict, List

from sqlalchemy import ARRAY, Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.core import ModelDAO
from gitdb.dao.models import Totals


class IssuesDAO(ModelDAO):
    """
    Prep Issues and Pulls data

    GitHub is giving us the information of both in the same
    API call, so we need to initialise them together
    """

    all: List[Dict[str, Any]]

    def __init__(
        self,
        client: APIClient,
        session: Session,
        base_instance: DeclarativeMeta,
        totals: Totals,
    ):
        super().__init__(client, session, base_instance)
        self.totals = totals

        class IssuesModel(base_instance):
            """
            Stars SQA model
            """

            __tablename__ = "issues"

            id = Column(Integer, primary_key=True)
            number = Column(Integer, primary_key=True)
            title = Column(String)
            body = Column(String)
            user_id = Column(Integer)  # Author
            user_login = Column(String)
            state = Column(String)
            assignees = Column(ARRAY(String))
            labels = Column(ARRAY(String))
            created_at = Column(DateTime)
            updated_at = Column(DateTime)
            closed_at = Column(DateTime)

            # https://docs.github.com/en/graphql/reference/enums#commentauthorassociation
            author_association = Column(String)
            html_url = Column(String)

        class PullsModel(base_instance):
            """
            Stars SQA model
            """

            __tablename__ = "pulls"

            id = Column(Integer, primary_key=True)
            number = Column(Integer, primary_key=True)
            title = Column(String)
            body = Column(String)
            user_id = Column(Integer)  # Author
            user_login = Column(String)
            state = Column(String)
            assignees = Column(ARRAY(String))
            requested_reviewers = Column(ARRAY(String))
            requested_teams = Column(ARRAY(String))
            labels = Column(ARRAY(String))
            created_at = Column(DateTime)
            updated_at = Column(DateTime)
            closed_at = Column(DateTime)
            merged_at = Column(DateTime)
            author_association = Column(String)
            html_url = Column(String)

        self._issues_model = IssuesModel
        self._pulls_model = PullsModel

    def load(self):
        self.all = self.client.get_all_parallel(
            self.client.repo_path / "issues",
            total=self.totals.total_pulls + self.totals.total_issues,
            option="&state=all",
            threads=16,
        )

    def transform(self) -> List[DeclarativeMeta]:
        # self._model.__table__.create(bind=self.session.bind)
        self.base.metadata.create_all(bind=self.session.bind)

        issues_data = [
            self._issues_model(
                id=elem["id"],
                number=elem["number"],
                user_id=elem["user"]["id"],
                user_login=elem["user"]["login"],
                title=elem["title"],
                body=elem["body"],
                state=elem["state"],
                labels=[label["name"] for label in elem["labels"]]
                if elem.get("labels")
                else None,
                assignees=[user["login"] for user in elem["assignees"]]
                if elem.get("assignees")
                else None,
                created_at=elem["created_at"],
                updated_at=elem["updated_at"],
                closed_at=elem["closed_at"],
                author_association=elem["author_association"],
                html_url=elem["html_url"],
            )
            for elem in self.all
            if elem.get("pull_request") is None
        ]

        pulls_data = [
            self._pulls_model(
                id=elem["id"],
                number=elem["number"],
                user_id=elem["user"]["id"],
                user_login=elem["user"]["login"],
                title=elem["title"],
                body=elem["body"],
                state=elem["state"],
                labels=[label["name"] for label in elem["labels"]]
                if elem.get("labels")
                else None,
                assignees=[user["login"] for user in elem["assignees"]]
                if elem.get("assignees")
                else None,
                requested_reviewers=[
                    label["login"] for label in elem["requested_reviewers"]
                ]
                if elem.get("requested_reviewers")
                else None,
                requested_teams=[label["name"] for label in elem["requested_teams"]]
                if elem.get("requested_teams")
                else None,
                created_at=elem["created_at"],
                updated_at=elem["updated_at"],
                closed_at=elem["closed_at"],
                merged_at=elem["pull_request"]["merged_at"],
                author_association=elem["author_association"],
                html_url=elem["html_url"],
            )
            for elem in self.all
            if elem.get("pull_request")
        ]

        return pulls_data + issues_data
