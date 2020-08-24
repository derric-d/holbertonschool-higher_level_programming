#!/usr/bin/env python3
"""script to fetch url header"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code > 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
