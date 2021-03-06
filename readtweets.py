from birdy.twitter import UserClient
from parser import Parser
import config
import sys

CONSUMER_KEY =  config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

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

def get_suggestion_categories (): #Gets official twitter suggested user categories
	categories = []
	response = client.api.users.suggestions.get()
	for suggestion in response.data:
		categories.append(suggestion.slug)
	return categories		

def get_names_from_category (slug): #Gets the names from those categories
	names = []
	response = client.api.users.suggestions[slug].members.get()
	for member in response.data:
		names.append(member.screen_name)
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


def get_variable_unclassified_data(slug, start, end): #Gets a variable amount of data from API for a particular user group - good to avoid rate limiting
	train = []
	test = []
	names = get_names_from_category (slug)
	for i in range(start,end):
		tweets = tweet_array(names[i])
		for j in range(0, len(tweets)):
			if j % 4 == 0:
				test.append(tweets[j])
			else:
				train.append(tweets[j])
	return train, test

def put_variable_segmented_data(slug, start, end): #Appends the data from a particular user group into the files in the ./data folder - 75% train, 25% test
	trainstring = './data/' + slug + 'train'
	teststring = './data/' + slug + 'test' 
	train = open(trainstring, 'a')
	test = open(teststring, 'a')
	trainlist, testlist = get_variable_unclassified_data(slug, start, end)
	for item in trainlist:
		print>>train, item
	for item in testlist:
		print>>test, item

