#!/usr/bin/python3
'''A module containing the State model.
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
"""Represents the base class for all tables"""


class State(Base):
    """Representation of a row in a states table"""
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        back_populates="state"
    )
