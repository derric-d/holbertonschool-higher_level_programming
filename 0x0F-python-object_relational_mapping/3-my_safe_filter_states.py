#!/usr/bin/python3
"""script to list all states from db"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
        usr, password, datab, state = argv[1], argv[2], argv[3], argv[4]
        db = MySQLdb.connect(host="localhost", user=usr,
                             password=password, db=datab)
        db = db.cursor()
        db.execute("""SELECT * FROM states
                   WHERE name=%s ORDER BY id""", (state,))

        states_ls = db.fetchall()
        for i in states_ls:
                print(i)
