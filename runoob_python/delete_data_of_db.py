#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE1 WHERE AGE > '%d'" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
