#!/usr/bin/env python3
"""script to fetch url header"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    load = {"q": argv[1][0] if len(argv) > 1 else ""}
    r = requests.post(url, data=load)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
