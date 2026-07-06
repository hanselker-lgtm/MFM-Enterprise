"""
Database session factory.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


class SessionFactory:

    def __init__(self, database_url: str):

        self.engine = create_engine(
            database_url,
            future=True,
            echo=False,
        )

        self._factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            class_=Session,
        )

    def create(self) -> Session:

        return self._factory()