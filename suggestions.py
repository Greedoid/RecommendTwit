import sqlite3
import json
from random import shuffle

def add_suggestion(handle, classification): #Adds a suggestion, which consists of a name and a class
	conn = sqlite3.connect('tweeters.db')
	conn.execute("INSERT INTO suggestions(Handle, Class) VALUES (?, ?)", (handle, classification),)
	conn.commit()
	if conn:
		conn.close()

def check_if_exists(handle): #Returns true or false based on whether it exists
	flag = 0;
	conn = sqlite3.connect('tweeters.db')
	cur = conn.cursor()
	cur.execute('SELECT * FROM suggestions WHERE Handle = ?', [handle])
	flag = (cur.fetchone() is not None)
	if conn:
		conn.close()
	return flag

def get_class(handle): # Retrieves the class of a particular suggestion
	conn = sqlite3.connect('tweeters.db')
	cur = conn.cursor()
	cur.execute("SELECT Class FROM suggestions WHERE Handle = ?", [handle])
	classified = cur.fetchone()
	if conn: 
		conn.close()
	return classified

def get_suggestions(classification): #Gets a suggestion from the DB
	conn = sqlite3.connect('tweeters.db')
	cur = conn.cursor()
	cur.execute("SELECT Handle FROM suggestions WHERE Class = ?", [classification])
	handles = cur.fetchall()
	shuffle(handles)
	toreturn = handles[:5]
	cleanedup = [str(elem[0]) for elem in toreturn]
	if conn: 
		conn.close()
	return cleanedup

def remove_suggestion(handle): #Removes one from teh DB
	conn = sqlite3.connect('tweeters.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM suggestions WHERE Handle = ?", [handle])
	if conn:
		conn.close()
