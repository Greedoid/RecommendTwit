import sqlite3


conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("CREATE TABLE suggestions(Handle VARCHAR NOT NULL PRIMARY KEY, tweets BLOB, class VARCHAR)")  #Inits with a twitter handle, their tweets, and their class
if conn:
	conn.close()
