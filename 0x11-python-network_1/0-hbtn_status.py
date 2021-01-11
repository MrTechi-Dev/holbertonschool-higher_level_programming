#!/usr/bin/python3
"""This script will fetches data from the website"""

from urllib import request

URL = "https://intranet.hbtn.io/status"
with request.urlopen(URL) as response:
    data = response.read()
    data_decode = data.decode('UTF-8')
    print('Body response: \n\t- type {}\n\t- content: {}\n\t- utf8 content: {}'
          .format(type(data), data, data_decode))
