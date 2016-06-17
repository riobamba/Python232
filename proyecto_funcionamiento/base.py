#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('disponiblidad.db')
print "Opened database successfully";

cursor = conn.execute("SELECT net, sta, fun  from funcionamiento")
for row in cursor:
   print "net = ", row[0]
   print "sta = ", row[1]
   print "fun = ", row[2], "\n"

print "Operation done successfully";
conn.close()