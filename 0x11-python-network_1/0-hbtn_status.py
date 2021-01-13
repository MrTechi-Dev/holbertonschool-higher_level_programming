#!/usr/bin/python3
"""This script will fetches data from the website"""

from urllib import request

if __name__ == "__main__":
    URL = "https://intranet.hbtn.io/status"
    with request.urlopen(URL) as response:
        html = response.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
