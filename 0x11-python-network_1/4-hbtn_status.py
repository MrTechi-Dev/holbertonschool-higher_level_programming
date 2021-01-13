#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    url = 'https://intranet.hbtn.io/status'
    result = requests.get(url)
    cont = result.text
    print("Body response:")
    print("\t- type:", type(result.content.decode('utf-8')))
    print("\t- content:", result.content.decode('utf-8'))
