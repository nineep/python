#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version: %s " % data)

db.close()
