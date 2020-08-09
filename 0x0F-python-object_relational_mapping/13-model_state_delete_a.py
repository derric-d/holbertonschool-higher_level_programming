#!/usr/bin/python3
"""use sqlalchemy to list states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    sess = Session(eng)
    query = sess.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for res in query:
        sess.delete(res)
    sess.commit()
    sess.close()
