#!/usr/bin/python3
"""script to get header"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as r:
        res = r.read()
        t = type(res)
        d = res.decode('utf-8')
        print(
            "Body\
            Response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
            .format(t, res, d))
