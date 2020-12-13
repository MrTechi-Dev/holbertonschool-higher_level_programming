#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute(("SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id;"))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
