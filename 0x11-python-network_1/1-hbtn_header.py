#!/usr/bin/python3
"""script to fetch url header"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as r:
            print(r.getheader("X-Request-Id"))
