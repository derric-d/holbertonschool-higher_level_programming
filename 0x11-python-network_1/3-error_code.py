#!/usr/bin/python3
"""script to fetch url header"""
from sys import argv as av
from urllib import request, parse, error


if __name__ == '__main__':
    try:
        with request.urlopen(av[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
