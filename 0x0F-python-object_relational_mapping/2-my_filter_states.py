#!/usr/bin/python3
"""
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    searched = argv[4]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cur = db.cursor()
    cur.execute("SELECT * FROM states  WHERE name LIKE BINARY'{}'\
                ORDER BY id;".format(searched))
    for x in cur.fetchall():
        print(x)
    db.close()
    cur.close()
