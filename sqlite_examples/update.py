# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test1.db')
c = conn.cursor()

c.execute('UPDATE COMPANY set SALARY = 250000.00 where ID=1')
conn.commit()

cursor = conn.execute('SELECT id, name, address, salary from COMPANY')
for row in cursor:
    print('ID=', row[0])
    print('NAME=', row[1])
    print('ADDRESS=', row[2])
    print('SALARY=', row[3], '\n')

print('Operation done successfully')
conn.close()
