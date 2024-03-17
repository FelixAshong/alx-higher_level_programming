#!/usr/bin/python3
"""lists all states from the database 'hbtn_0e_0_usa'"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for data in cursor.fetchall():
        print(data)
    cursor.close()
    db.close()
