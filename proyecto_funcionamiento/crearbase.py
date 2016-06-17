#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('disponiblidad.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE funcionamiento(net VARCHAR, sta VARCHAR, loc VARCHAR, lat VARCHAR, lon VARCHAR, fun VARCHAR, tipo VARCHAR,fecha VARCHAR);''')
print "Table created successfully";

conn.close()