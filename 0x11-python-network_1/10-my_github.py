#!/usr/bin/env python3
"""script to fetch url header"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://api.github.com/user"
    load = (argv[1], argv[2])
    r = requests.post(url, auth=load)
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
