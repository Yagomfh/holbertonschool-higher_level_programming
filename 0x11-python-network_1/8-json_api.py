#!/usr/bin/python3
"""that takes in a letter and sends a POST request"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://577da9f9ae6a.0a98cdc3.hbtn-cod.io:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    data = {'q': q}
    rep = requests.post(url, data=data)
    if rep.text == '{}\n':
        print('No result')
    else:
        try:
            data = rep.json()
            print("[{}] {}".format(data['id'], data['name']))
        except:
            print("Not a valid JSON")
