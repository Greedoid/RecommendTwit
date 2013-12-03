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
from suggestions import get_tweets

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
	
X_train, y_train_text = get_train_as_nparray() 
X_test = get_tweets('Perry_Huang')

categories = Reader.get_suggestion_categories();
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
predicted = classifier.predict(X_test)
all_labels = lb.inverse_transform(predicted)
print all_labels

#for item, labels in zip(X_test, all_labels):
#	print '%s => %s' % (item, ', '.join(labels))
#print accuracy_score(all_labels, y_test_text)
