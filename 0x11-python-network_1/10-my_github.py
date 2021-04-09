#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        r = requests.get(url, auth=(username, password))
        print(r.json()['id'])
    except:
        print("None")
