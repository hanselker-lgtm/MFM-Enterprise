"""
Base class for child entities.
"""

from mfm.database.base import Base


class Entity(Base):

    __abstract__ = True