#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    c = requests.get(url)
    j = c.json()
    try:
        for i in range(10):
            print("{}: {}".format(j[i].get('sha'),
                  j[i].get('commit').get('author').get('name')))
    except:
        pass
