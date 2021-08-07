#!/usr/bin/python3
''' Lists all states from the databases '''


import MySQLdb
from sys import argv
if __name__ == '__main__':

    connection = MySQLdb.connect(user=argv[1],
                                 passwd=argv[2],
                                 connection=argv[3],
                                 host="localhost",
                                 port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    states = cursor.fetchall()
    for row in states:
        print(state)
    cursor.close()
    connection.close()
