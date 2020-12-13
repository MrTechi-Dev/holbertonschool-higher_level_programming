#!/usr/bin/python3
"""
script that list all states.id  with name starting with N from
database hbtn_0e_0_usa.
"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    user_name = sys.argv[1]
    passw = sys.argv[2]
    data_base = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user_name, passwd=passw, db=data_base)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC ")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
