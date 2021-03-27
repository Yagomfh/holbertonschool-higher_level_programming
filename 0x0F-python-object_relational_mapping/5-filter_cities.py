#!/usr/bin/python3
"""Module get all states"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    states = cur.execute("SELECT cities.id, cities.name, states.name\
                          FROM cities JOIN states\
                          ON cities.state_id = states.id\
                          ORDER BY cities.id")
    result = cur.fetchall()
    matches = ""
    for row in result:
        if row[2] == sys.argv[4]:
            matches += row[1] + ', '
    print(matches.rstrip(", "))
