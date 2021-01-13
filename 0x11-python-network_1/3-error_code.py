#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays 
the body of the response (decoded in utf-8)."""

if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    URL = argv[1]
    try:
        with request.urlopen(URL) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.getcode())
