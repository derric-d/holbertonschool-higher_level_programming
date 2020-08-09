#!/usr/bin/python3
"""script to list all states from db"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    usr, password, datab, states = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost", user=usr,
                         password=password, db=datab)
    db = db.cursor()
    db.execute("""SELECT cities.name
                FROM cities JOIN states
                ON state_id= states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id""", (states,))

    states_ls = db.fetchall()
    print(", ".join([i[0] for i in states_ls]))
