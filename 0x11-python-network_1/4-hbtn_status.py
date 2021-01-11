#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    url =  'https://intranet.hbtn.io/status'
    result = requests.get(url)
    cont = result.text
    print('Body response: \n\t- type: {}\n\t- content: {}'
           .format(type(cont), cont))
