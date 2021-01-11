#!/usr/bin/python3
""" Python script that takes in a URL, sends a 
request to the URL and displays the body of the response"""

import requests
from sys import argv

if __name__ == "__main__":
    URL = argv[1]
    req = requests.get(URL)
    if req.status_code == 200:
        print(req.content.decode('utf-8'))
    else:
        print("Error code:", req.status_code)