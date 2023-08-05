"""
Handle stars data
"""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, Sequence, String
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient
from gitdb.dao.core import ModelDAO
from gitdb.dao.models import Totals

SEARCH_QUERY_LIMIT = 1000
QUERY = """
query PaginatePulls($search_query: String!, $first: Int, $after: String) {
  search(query: $search_query, type: ISSUE, first: $first, after: $after) {
    edges {
      node {
        ... on PullRequest {
          number
          reviews(last: 10) {
            nodes {
              author {
                login
              }
              state
              publishedAt
            }
          }
        }
      }
    }
  }
}
"""


class ReviewsAggModel(BaseModel):
    """Tmp model with array of elements"""

    number: int
    reviewer: Optional[List[str]]
    review_state: Optional[List[str]]
    reviewed_at: Optional[List[str]]


class ReviewsDAO(ModelDAO):
    """
    Prep Review data
    """

    data: List[Dict[str, Any]]

    def __init__(
        self,
        client: APIClient,
        session: Session,
        base_instance: DeclarativeMeta,
        totals: Totals,
    ):
        super().__init__(client, session, base_instance)
        self.totals = totals

        class ReviewsModel(base_instance):
            """
            Reviews SQA model
            """

            __tablename__ = "latest_reviews"

            id = Column(Integer, Sequence("review_id_seq"), primary_key=True)
            number = Column(Integer)
            reviewer = Column(String)
            review_state = Column(String)
            reviewed_at = Column(DateTime)

        self._model = ReviewsModel

    def load(self):
        self.data = self.client.get_all_search_query_parallel(
            query=QUERY,
            search_query=f"is:pr base:main repo:{self.client.config.owner}/{self.client.config.repo}",
            total=min(self.totals.total_pulls, SEARCH_QUERY_LIMIT),
            threads=3,
        )

    def transform(self) -> List[DeclarativeMeta]:
        # self._model.__table__.create(bind=self.session.bind)
        self.base.metadata.create_all(bind=self.session.bind)

        tmp_model = [
            ReviewsAggModel(
                number=elem["number"],
                reviewer=[
                    review["author"]["login"] for review in elem["reviews"]["nodes"]
                ]
                if elem.get("reviews") and elem["reviews"].get("nodes")
                else None,
                review_state=[review["state"] for review in elem["reviews"]["nodes"]]
                if elem.get("reviews") and elem["reviews"].get("nodes")
                else None,
                reviewed_at=[
                    review["publishedAt"] for review in elem["reviews"]["nodes"]
                ]
                if elem.get("reviews") and elem["reviews"].get("nodes")
                else None,
            )
            for elem in self.data
        ]

        # reviewer, review_state and reviewed_at have the same length
        data = [
            self._model(
                number=row.number,
                reviewer=row.reviewer[idx],
                review_state=row.review_state[idx],
                reviewed_at=row.reviewed_at[idx],
            )
            for row in tmp_model
            if row.reviewer
            for idx in range(len(row.reviewer))
        ]

        return data
