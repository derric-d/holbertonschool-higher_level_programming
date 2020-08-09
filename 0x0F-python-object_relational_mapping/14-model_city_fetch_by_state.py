#!/usr/bin/python3
"""use sqlalchemy to list states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    res = sess.query(City, State).filter(
        City.state_id == State.id).all()
    for city, state in res:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    sess.commit()
    sess.close()
