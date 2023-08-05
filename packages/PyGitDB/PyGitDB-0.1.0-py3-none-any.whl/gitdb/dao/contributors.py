"""
Handle stars data
"""
from typing import Any, Dict, List

from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.core import ModelDAO


class ContributorsDAO(ModelDAO):
    """
    Prep Stars data
    """

    contributors: List[Dict[str, Any]]

    def __init__(
        self, client: APIClient, session: Session, base_instance: DeclarativeMeta
    ):
        super().__init__(client, session, base_instance)

        class ContributorsModel(base_instance):
            """
            Stars SQA model
            """

            __tablename__ = "contributors"

            id = Column(Integer, Sequence("contributors_id_sequence"), primary_key=True)
            contributions = Column(Integer)
            user_id = Column(Integer)
            user_login = Column(String)

        self._model = ContributorsModel

    def load(self):
        self.contributors = self.client.get_all_simple(
            self.client.repo_path / "contributors"
        )

    def transform(self) -> List[DeclarativeMeta]:
        self.base.metadata.create_all(bind=self.session.bind)

        data = [
            self._model(
                contributions=elem["contributions"],
                user_id=elem["id"],
                user_login=elem["login"],
            )
            for elem in self.contributors
        ]

        return data
