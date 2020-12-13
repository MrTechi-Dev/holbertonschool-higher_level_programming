#!/usr/bin/python3
"""
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    user_name = sys.argv[1]
    passw = sys.argv[2]
    data_base = sys.argv[3]
    word = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user_name, passwd=passw, db=data_base)
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name='{}'ORDER BY id;".format(word))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
