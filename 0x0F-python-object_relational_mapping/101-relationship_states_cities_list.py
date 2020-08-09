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
    states = sess.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    sess.commit()
    sess.close()
