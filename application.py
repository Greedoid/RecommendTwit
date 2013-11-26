from flask import Flask
from flask import render_template
from classify import get_readability_index as get_level
import json
import readtweets as Reader
from tweetgetter import TweetForm

app = Flask(__name__)
app.config.from_object('config') #Need to have a secret key for WTForms

@app.route('/') #Simple page, serves up index with a WTForm
def index():
	form = TweetForm()
	return render_template('index.html',
			form = form)

@app.route('/tweets/<handle>', methods=['GET']) #Actually gets tweets - called asynchronously via jQuery
def get_tweets_from_handle(handle):
	array = Reader.tweet_array(handle)
	return json.dumps(array)

@app.route('/level/<handle>', methods=['GET']) #Calculated automated reading level using classify.py - called asynch via jQuery
def get_reader_level_from_handle(handle):
	print str(get_level(handle))
	return str(get_level(handle))

if __name__ == '__main__':
	app.debug = True
	app.run()
