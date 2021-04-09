#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import requests
import sys


url = sys.argv[1]
r = requests.get(url)
if int(r.status_code) >= 400:
    print(r.status_code)
else:
    print(r.text)
