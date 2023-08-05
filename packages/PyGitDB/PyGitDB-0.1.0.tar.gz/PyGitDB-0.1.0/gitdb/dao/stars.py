"""
Handle stars data
"""
from typing import Any, Dict, List

from sqlalchemy import Column, DateTime, Integer, Sequence, String
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.core import ModelDAO
from gitdb.dao.models import Totals


class StarsDAO(ModelDAO):
    """
    Prep Stars data
    """

    stars: List[Dict[str, Any]]

    def __init__(
        self,
        client: APIClient,
        session: Session,
        base_instance: DeclarativeMeta,
        totals: Totals,
    ):
        super().__init__(client, session, base_instance)
        self.totals = totals

        class StarsModel(base_instance):
            """
            Stars SQA model
            """

            __tablename__ = "stargazers"

            id = Column(Integer, Sequence("stargazers_id_sequence"), primary_key=True)
            starred_at = Column(DateTime)
            user_id = Column(Integer)
            user_login = Column(String)

        self._model = StarsModel

    def load(self):
        self.stars = self.client.get_all_parallel(
            self.client.repo_path / "stargazers",
            total=self.totals.total_stars,
        )

    def transform(self) -> List[DeclarativeMeta]:
        self.base.metadata.create_all(bind=self.session.bind)

        data = [
            self._model(
                starred_at=elem["starred_at"],
                user_id=elem["user"]["id"],
                user_login=elem["user"]["login"],
            )
            for elem in self.stars
        ]

        return data
