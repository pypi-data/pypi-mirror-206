"""
Define common Models
"""
from typing import Optional

from pydantic import BaseModel


class Totals(BaseModel):
    """Total values to be queries"""

    total_stars: int
    total_issues: int
    total_pulls: int


class QueryVariables(BaseModel):
    """Query variables to pass"""

    search_query: str
    first: int
    after: Optional[str]
