#!/usr/bin/python3
"""script to list all states from db"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
        usr, password, datab = argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host="localhost", user=usr,
                             password=password, db=datab)
        db = db.cursor()
        db.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities, states
                   WHERE cities.state_id = states.id
                   ORDER BY id""")

        states_ls = db.fetchall()
        for i in states_ls:
                print(i)
