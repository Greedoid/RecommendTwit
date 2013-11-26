import readtweets as Reader
import suggestions as DB
import re

def readability_index(tweetstring): #Calculate the automated readability index of the aggregated tweet string
	sentence_array = re.split(r'[.!]+', tweetstring) #Counts !!!! as 4 sentences - surprisingly useful
	characters = len(tweetstring)
	words = 0
	sentences = len(sentence_array)
	for sent in sentence_array:
		words = words + len(sent.split(' '))
	index = 4.71*(float(characters)/float(words)) + 0.5*(float(words)/float(sentences)) - 21.43
	print characters
	print words
	print sentences
	return index

def get_readability_index(name): #Actual method to call - checks to see if name is in DB - if so, get db value. if not, go through the motions calculating
	if DB.check_if_exists(name):
		return DB.get_reading_level(name)
	else:
		index = readability_index(Reader.tweet_sentence(name))
		DB.add_complete_suggestion(name, index, Reader.tweet_array(name))	
		print index
		return index
	
