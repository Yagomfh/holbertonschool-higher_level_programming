#!/usr/bin/python3
"""Module to print type, content and utf8 content of body response"""
import urllib.request


url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
