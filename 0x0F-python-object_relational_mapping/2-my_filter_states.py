#!/usr/bin/python3

"""displays all values in the states table of hbtn_0e_0_usa
   where name matches matches an argument passed as a parameter"""

import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        state_name = sys.argv[4]
        cursor.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
        )
        for data in cursor.fetchall():
            print(data)
        cursor.close()
        db_connection.close()
