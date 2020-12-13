#!/usr/bin/python3
"""
contains the class definition of a City and
an instance Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class City
    Args:
        Base (Super class): Instance of declarative_base
        function that constructs a base
        class for declarative class definitions.
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False, unique=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
