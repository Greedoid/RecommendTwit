from birdy.twitter import UserClient
from parser import Parser
import sys

CONSUMER_KEY = 'j1cEpIci2OYJwY9bGnpYjg' 					#These are needed for the API call
CONSUMER_SECRET = 'j6KxJuUAO9rzY5c7Z4FC89a9USzaKvvawnmrqiPwxg'
ACCESS_TOKEN = '1398624751-cryJwzYXQBtG6wHJephlHcvggNtpshs3Qvu4ADW'
ACCESS_TOKEN_SECRET = 'xlPzEl2zHOqMNmuEIYfRvBu2qkuziEOkvTY3gANcSy7Sj'
LONG_LONG_MAX = 9223372036854775807
MAGIC_NUMBER = LONG_LONG_MAX/10 #Twitter API will not take long long, but a long long / 10 will be bigger than any tweet ID - only used for ease of iteration


client = UserClient(CONSUMER_KEY,
		CONSUMER_SECRET,
		ACCESS_TOKEN,
		ACCESS_TOKEN_SECRET)

def tweet_array (name): #Does what print_all does, but returns an array
	tweets = []
	request = client.api.statuses.user_timeline
	min_id = MAGIC_NUMBER
	for x in range (0, 15):
		response = request.get(screen_name = name, count = 200, trim_user = 1, include_rts = 0, max_id = min_id)
		parser = Parser(response.data)
		min_id = parser.get_min_id()
		for z in range (0, len(response.data)):
			if (parser.get_text(z) != ''):
				tweets.append(parser.get_text(z))
	return tweets

def tweet_sentence (name): #Does what print_all does, but returns one long string - useful for calculating the readability index
	tweets = ''
	request = client.api.statuses.user_timeline
	min_id = MAGIC_NUMBER
	for x in range (0, 15):
		response = request.get(screen_name = name, count = 200, trim_user = 1, include_rts = 0, max_id = min_id)
		parser = Parser(response.data)
		min_id = parser.get_min_id()
		for z in range (0, len(response.data)):
			if (parser.get_text(z) != ''):
				tweets = tweets + (parser.get_text(z)) + '.'
	return tweets

def get_suggestion_categories ():
	categories = []
	response = client.api.users.suggestions.get()
	for suggestion in response.data:
		categories.append(suggestion.slug)
	return categories		

def get_names_from_category (slug):
	names = []
	response = client.api.users.suggestions[slug].members.get()
	for member in response.data:
		names.append(member.name)
	return names

def get_unclassified_data(slug): #Simply gets all tweets from a category and  
	train = []
	test = []
	for name in get_names_from_category(slug):
		tweets = tweet_array(name)
		for j in range(0, len(tweets)):
			if j % 4 == 0:
				test.append(tweets[j])
			else:
				train.append(tweets[j])
	return train, test

def get_tiny_unclassified_data(slug):
	train = []
	test = []
	names = get_names_from_category (slug)
	for i in range(0,2):
		tweets = tweet_array(names[i])
		for j in range(0, len(tweets)):
			if j % 4 == 0:
				test.append(tweets[j])
			else:
				train.append(tweets[j])
	return train, test

def put_tiny_segmented_data(slug):
	trainstring = './data/' + slug + 'train'
	teststring = './data/' + slug + 'test' 
	train = open(trainstring, 'w')
	test = open(teststring, 'w')
	trainlist, testlist = get_tiny_unclassified_data(slug)
	for item in trainlist:
		print>>train, item
	for item in testlist:
		print>>test, item


def put_segmented_data(slug):
	trainstring = './data/' + slug + 'train'
	teststring = './data/' + slug + 'test' 
	train = open(trainstring, 'w')
	test = open(teststring, 'w')
	trainlist, testlist = get_tiny_unclassified_data(slug)
	for item in trainlist:
		print>>train, item
	for item in testlist:
		print>>test, item

