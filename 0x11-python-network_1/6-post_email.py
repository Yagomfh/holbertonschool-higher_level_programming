#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response"""
import requests
import sys


url = sys.argv[1]
data = {'email': sys.argv[2]}
req = requests.post(url, data=data)
print(req.text)
