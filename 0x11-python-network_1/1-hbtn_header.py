#!/usr/bin/python3
"""Script that reads the header of a request"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
