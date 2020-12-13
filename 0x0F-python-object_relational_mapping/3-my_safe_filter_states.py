#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
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
                WHERE name=%s ORDER BY states.id""", (word,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
