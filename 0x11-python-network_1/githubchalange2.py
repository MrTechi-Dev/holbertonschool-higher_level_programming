#!/usr/bin/python3
"""Write a Python script that takes 2 arguments
in order to solve this challenge
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    URL = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    res = requests.get(URL)

    commits = res.json()

    for c in commits[:10]:
        sha = c.get('sha')
        author = c.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
