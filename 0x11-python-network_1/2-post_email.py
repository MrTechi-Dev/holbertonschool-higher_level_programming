#!/usr/bin/python3
"""Script that takes the url and an email, send a POST
request to the passed URL and displays the boy of the respomse"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('UTF-8'))
