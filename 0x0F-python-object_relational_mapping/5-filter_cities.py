#!/usr/bin/python3
"""Lists all states from the databases"""


import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id", (argv[4], ))
    query_rows = cur.fetchall()
    first = 0
    for row in query_rows:
        if first != 0:
            print(", ", end="")
        print("%s" % row, end="")
        first += 1
    print("")
    cur.close()
    conn.close()
