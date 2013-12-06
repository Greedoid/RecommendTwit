from flask import Flask
from flask import render_template
import json
import readtweets as Reader
from classifier import SVM
from tweetgetter import TweetForm


Classifier = SVM()
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

@application.route('/suggestions/<handle>', methods=['GET']) #Gets the user some people to follow
def get_suggestions_from_handle(handle):
	suggestions = Classifier.get_user_suggestions(handle)
	return json.dumps(suggestions)

if __name__ == '__main__':
	application.debug = True
	application.run(host='0.0.0.0', debug=True)
