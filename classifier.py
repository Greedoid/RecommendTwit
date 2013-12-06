import readtweets as Reader
import suggestions as DB
import re
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from classio import *
from readtweets import tweet_array, get_suggestion_categories
from suggestions import add_suggestion, get_suggestions


#This is where the magic happens. Uses scikit learn to train a multiclass SVM on all of our training data

class SVM:
	def __init__(self):
		self.classifier, self.bin_labels = make_svm()

	def classified_tweets(self, handle): #Gets classified tweets from a specific user
		predicted = self.classifier.predict(tweet_array(handle))
		labels = self.bin_labels.inverse_transform(predicted)
		return labels
	
	def label_dict(self, handle): #Assemble classified tweets in a dict for ease of readability - see what the top ones are
		l_dict = {}
		predicted = self.classifier.predict(tweet_array(handle))
		labels = self.bin_labels.inverse_transform(predicted)
		for raw_label in labels:
			if raw_label:
				label = str(raw_label[0])	
				if label in l_dict.keys():
					l_dict[label] = l_dict[label] + 1
				else:
					l_dict[label] = 0
		return l_dict
	
	def get_ratios(self, handle): #Useful for debugging - makes seeing how peoples tweets are classified easier
		ratio_dict = {}
		l_dict = self.label_dict(handle)
		total = sum(l_dict.itervalues())
		for key, value in l_dict.iteritems():
			ratio_dict[key] = float(value)/float(total)
		return ratio_dict

	def classify_handle(self, handle): #Classifies a twitter handle by assigning it the class the highest amount of their tweets was classified as
		labels = self.label_dict(handle)
		return max(labels, key = labels.get)

	def classify_suggestion_and_store(self, suggestion): #Stores suggestions - done manually right now. 
		classification = self.classify_handle(suggestion)
		add_suggestion(suggestion, classification)

	def get_user_suggestions(self, user): #This one is called by the frontend - returns from the DB usernames that are the same class
		user_class = self.classify_handle(user)
		handles = get_suggestions(user_class)
		return handles
		

				
def make_svm(): #Trains the SVM
	X_train, y_train_text = get_train_as_nparray() 

	categories = Reader.get_suggestion_categories(); #TODO cache API call
	target_names = []
	for item in categories:
		target_names.append([str(item)])

	lb = preprocessing.LabelBinarizer()
	Y = lb.fit_transform(y_train_text)

	classifier = Pipeline([
    	('vectorizer', CountVectorizer()),
    	('tfidf', TfidfTransformer()),
    	('clf', OneVsRestClassifier(LinearSVC()))])

	classifier.fit(X_train, Y)

	return classifier, lb


