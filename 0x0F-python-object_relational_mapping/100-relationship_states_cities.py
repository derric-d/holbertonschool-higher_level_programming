#!/usr/bin/python3
"""use sqlalchemy to list states"""
from sys import argv
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    state = State(name="California")
    city = City(name="San Francisco", state_id=state.id)
    state.cities.append(city)
    sess.add(state)
    sess.add(city)
    sess.commit()
    sess.close()
