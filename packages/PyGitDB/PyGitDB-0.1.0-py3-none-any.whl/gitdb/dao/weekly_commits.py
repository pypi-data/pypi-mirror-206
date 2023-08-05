"""
Handle commit data
"""
from datetime import datetime, timedelta
from typing import Dict, List

from sqlalchemy import Column, DateTime, Integer, Sequence
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.core import ModelDAO


class WeeklyCommitsDAO(ModelDAO):
    """
    Prep Stars data
    """

    commits: List[int]

    def __init__(
        self, client: APIClient, session: Session, base_instance: DeclarativeMeta
    ):
        super().__init__(client, session, base_instance)

        class WeeklyCommitsModel(base_instance):
            """
            Commits SQA model.

            Will store the last 52 weeks of commits.
            """

            __tablename__ = "weekly_commits"

            id = Column(Integer, Sequence("commits_id_sequence"), primary_key=True)
            date = Column(DateTime)
            commits = Column(Integer)

        self._model = WeeklyCommitsModel

    def load(self):
        _commits: Dict[str, List[int]] = self.client.get_all_simple(
            self.client.repo_path / "stats" / "participation"
        )

        self.commits = _commits["all"]

    def transform(self) -> List[DeclarativeMeta]:
        self.base.metadata.create_all(bind=self.session.bind)

        # Today minus days from Sunday
        last_sunday = datetime.today() - timedelta(
            days=datetime.today().isoweekday() % 7
        )

        # Prepare dates
        dates = [(last_sunday - timedelta(weeks=1 * i)) for i in range(52)]
        dates.reverse()

        data = [
            self._model(
                date=date,
                commits=self.commits[index],
            )
            for index, date in enumerate(dates)
        ]

        return data
