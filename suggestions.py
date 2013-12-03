import sqlite3
import json

def add_suggestion(handle, level): #Does the actual inserting of a suggested person to follow
	conn = sqlite3.connect('users.db')
	conn.execute("INSERT INTO suggestions(Handle, Reading_Level) VALUES(?, ?)", (handle, level),)
	conn.commit()
	if conn:
		conn.close()

def add_complete_suggestion(handle, level, tweets):
	conn = sqlite3.connect('users.db')
	tweetblob = buffer(json.dumps(tweets))
	conn.execute("INSERT INTO suggestions(Handle, Reading_Level, tweets) VALUES (?, ?, ?)", (handle, level, tweetblob),)
	conn.commit()
	if conn:
		conn.close()

def add_suggestion(handle, tweets, classification):
	conn = sqlite3.connect('users.db')
	tweetblob = buffer(json.dumps(tweets))
	conn.execute("INSERT INTO suggestions(Handle, Tweets, Class) VALUES (?, ?, ?)", (handle, tweetblob, classification),)
	conn.commit()
	if conn:
		conn.close()

def check_if_exists(handle): #Returns true or false based on whether it exists
	flag = 0;
	conn = sqlite3.connect('users.db')
	cur = conn.cursor()
	cur.execute('SELECT * FROM suggestions WHERE Handle = ?', [handle])
	flag = (cur.fetchone() is not None)
	if conn:
		conn.close()
	return flag

def get_reading_level(handle): #DB call - gets the level based on the passed handle
	conn = sqlite3.connect('users.db')
	cur = conn.cursor()
	cur.execute("SELECT Reading_Level FROM suggestions WHERE Handle = ?", [handle]) 
	level =  cur.fetchone()[0]
	if conn:
		conn.close()
	return level

def add_tweets(handle, tweets): #Stores tweets as a blob of JSON - to get back, convert to string and then that string to list
	conn = sqlite3.connect('users.db')
	tweetblob = buffer(json.dumps(tweets))
	conn.execute("INSERT INTO suggestions(Handle, Reading_Level, tweets) VALUES (?, ?, ?)", (handle, 333, tweetblob),)
	conn.commit()
	if conn:
		conn.close()

def get_tweets(handle):
	conn = sqlite3.connect('users.db')
	cur = conn.cursor()
	cur.execute("SELECT tweets FROM suggestions WHERE Handle = ?", [handle])
	tweets = cur.fetchone()[0]
	tweetarray = eval(str(tweets))
	if conn: 
		conn.close()
	return tweetarray
