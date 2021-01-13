#!/usr/bin/python3
"""Python script that takes your Github credentials
(username and password) and uses the Github API to display your id"""

if __name__ == '__main__':
    import requests
    import sys

    if __name__ == '__main__':

        username = sys.argv[1]
        passwd = sys.argv[2]
        response = requests.get('https://api.github.com/user',
                                auth=(username, passwd))
        print(response.json().get('id'))
