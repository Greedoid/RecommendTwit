from flask import Flask
from flask import render_template
from classify import get_readability_index as get_level
import json
import readtweets as Reader
import classify as Classifier
from tweetgetter import TweetForm

application = Flask(__name__)
application.config.from_object('config') #Need to have a secret key for WTForms

@application.route('/') #Simple page, serves up index with a WTForm
def index():
	form = TweetForm()
	return render_template('index.html',
			form = form)

@application.route('/tweets/<handle>', methods=['GET']) #Actually gets tweets - called asynchronously via jQuery
def get_tweets_from_handle(handle):
	array = Reader.tweet_array(handle)
	return json.dumps(array)

@application.route('/level/<handle>', methods=['GET']) #Calculated automated reading level using classify.py - called asynch via jQuery
def get_reader_level_from_handle(handle):
	return str(get_level(handle))

@application.route('/followers/<handle>', methods=['GET']) #Gets the user some people to follow
def get_suggestions_from_handle(handle):
	array = Classifier.get_suggestions(handle)
	return json.dumps(array)

if __name__ == '__main__':
	application.debug = True
	application.run(host='0.0.0.0', debug=True)
