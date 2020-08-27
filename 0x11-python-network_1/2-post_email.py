#!/usr/bin/python3
"""script to fetch url header"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    load = parse.urlencode({"email": argv[2]}).encode('ascii')
    with request.urlopen(argv[1], load) as r:
        res = r.read()
        print(res.decode('utf-8'))
