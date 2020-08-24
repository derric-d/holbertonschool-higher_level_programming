#!/usr/bin/python3
"""script to fetch url header"""
from urllib import request, parse
from sys import argv as av


if __name__ == '__main__':
    load = parse.urlencode({"email": av[2]}).encode()
    with request.urlopen(av[1], load) as r:
        print(r.read().decode('utf-8'))
