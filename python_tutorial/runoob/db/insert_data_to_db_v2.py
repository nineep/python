#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

sql = "INSERT INTO EMPLOYEE1( \
        FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
        VALUES('%s', '%s', '%d', '%c', '%d')" \
        % ('Mac', 'Mohan', 20, 'M', 2000)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
