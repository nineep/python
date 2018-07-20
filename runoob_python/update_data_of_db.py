#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

sql = "UPDATE EMPLOYEE1 SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
