#!/usr/bin/python3
"""sends a request to the URL
   displays the value of the variable X-Request-Id in the response header"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]
    r = get(url)
    print(r.headers.get("X-Request-Id"))
