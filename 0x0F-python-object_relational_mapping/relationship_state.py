#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Class State
    Args:
        Base (Super class): Instance of declarative_base
        function that constructs a base
        class for declarative class definitions.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128),
                  nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
