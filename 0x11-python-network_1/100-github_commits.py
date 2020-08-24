#!/usr/bin/python3
"""script to fetch url header"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    repo = argv[1]
    user = argv[2]
    url = "http://api.github.com/repos/{}/{}/commits".format(user, repo)
    r = requests.get(url)
    res = r.json()
    for entry in res[:10]:
        print("{}: {}".format(entry.get("sha"),
                              entry.get("commit").get("author").get("name")))
