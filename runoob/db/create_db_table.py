#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE1")

sql = """CREATE TABLE EMPLOYEE1(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""

cursor.execute(sql)

db.close()
