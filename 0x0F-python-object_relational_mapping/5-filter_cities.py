#!/usr/bin/python3
"""takes in the name of a state as an argument and
   lists all cities of that state, using the database 'hbtn_0e_4_usa'"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                   FROM cities JOIN states ON cities.state_id = states.id
                   WHERE states.name = %(state)s""", {'state': argv[4]})
    result = cursor.fetchall()
    length = len(result)
    if length == 0:
        print('')
    for i in range(length):
        if i < length - 1:
            print(result[i][0], end=', ')
        else:
            print(result[i][0])
    cursor.close()
    db.close()
