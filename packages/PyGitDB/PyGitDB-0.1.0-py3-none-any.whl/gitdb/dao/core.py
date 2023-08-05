"""
Model abs definition
"""
from abc import ABC, abstractmethod

from loguru import logger
from sqlalchemy.orm import DeclarativeMeta, Session

from gitdb.api.client import APIClient


class ModelDAO(ABC):
    """
    Core definition for stats models
    """

    def __init__(
        self, client: APIClient, session: Session, base_instance: DeclarativeMeta
    ):
        self.client = client
        self.session = session
        self.base = base_instance

    @abstractmethod
    def load(self):
        """Load the model data from the GitHub API"""

    @abstractmethod
    def transform(self):
        """Save the data into DuckDB"""

    def process(self) -> str:
        """
        Returns: the class name being processed
        """
        logger.info(f"Starting to process {self.__class__.__name__}...")
        self.load()
        return self.transform()
