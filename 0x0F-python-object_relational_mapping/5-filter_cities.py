#!/usr/bin/python3
""" ℹ️
    takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":

    import sys
    import MySQLdb

    user_name = sys.argv[1]
    passw = sys.argv[2]
    data_base = sys.argv[3]
    word = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=passw, db=data_base)
    cur = db.cursor()
    cur.execute("SELECT city.name FROM states as state\
                join cities as city ON state.id = city.state_id\
                where state.name =%s", (word,))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
        i += 1
    print()
    cur.close()
    db.close()
