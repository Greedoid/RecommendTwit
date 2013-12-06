import sqlite3


conn = sqlite3.connect('tweeters.db')
c = conn.cursor()
c.execute("CREATE TABLE suggestions(Handle VARCHAR NOT NULL PRIMARY KEY, class VARCHAR)")  #Inits with a twitter handle, their tweets, and their class
c.execute("CREATE TABLE user(Handle VARCHAR NOT NULL PRIMARY KEY, blacklist BLOB)")
if conn:
	conn.close()
