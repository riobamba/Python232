#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('disponiblidad.db')
print "Opened database successfully";

cursor = conn.execute("SELECT net, sta, fun,fecha from funcionamiento")
for row in cursor:
   print "net = ", row[0]
   print "sta = ", row[1]
   print "sta = ", row[2]
   print "fun = ", row[3], "\n"

print "Operation done successfully";
conn.close()