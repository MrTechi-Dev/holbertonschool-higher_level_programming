#!/usr/bin/python3
"""
script that list all states.id  with name starting with N from
database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id;")
    for x in cr.fetchall():
        print(x)
    cr.close()
    db.close()
