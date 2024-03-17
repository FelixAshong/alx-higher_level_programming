#!/usr/bin/python3
"""sends a POST request to the passed URL with the passed email as a parameter
   Displays the body of the response (decoded in utf-8)"""
import urllib.parse as parse
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
