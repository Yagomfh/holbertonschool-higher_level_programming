#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()


def sql_query():
    """SQL query"""
    states = cur.execute("SELECT * FROM states ORDER BY id")
    result = cur.fetchall()
    for row in result:
        if row[1][0] == 'N':
            print(row)

if __name__ == '__main__':
    sql_query()
