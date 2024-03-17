#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
   uses the GitHub API to display your id"""
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    request = get("https://api.github.com/user", auth=credentials)
    print(request.json().get("id"))
