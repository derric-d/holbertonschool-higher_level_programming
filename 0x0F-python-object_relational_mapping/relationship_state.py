#!/usr/bin/python3
"""define state class and base"""
from sqlalchemy import Column, Integer, String
from relationship_city import City, Base
from sqlalchemy.orm import relationship


class State(Base):
    """State def"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
