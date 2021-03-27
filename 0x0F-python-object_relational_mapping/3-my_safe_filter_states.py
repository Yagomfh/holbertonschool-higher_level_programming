#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    states = cur.execute("SELECT * FROM states WHERE name = %(state)s ORDER \
BY states.id ASC", {'state': sys.argv[4]})
    result = cur.fetchall()
    for row in result:
        print(row)
