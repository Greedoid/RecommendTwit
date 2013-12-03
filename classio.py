import glob
import numpy as np

def get_all_data(): #Basic file i/o, read train and test data and output arrays of each
	test = []
	train = []
	testfiles = glob.glob('./data/*test')
	for varfile in testfiles:
		f = open(varfile, 'r')
		textclass = varfile.replace('./data/', '')
		textclass = textclass.replace('test', '')
		for line in f.readlines():
			test.append((line.strip(), textclass))
		f.close()
	trainfiles = glob.glob('./data/*train')
	for varfile in trainfiles:
		f = open(varfile, 'r')
		textclass = varfile.replace('./data/', '')
		textclass = textclass.replace('train', '')
		for line in f.readlines():
			train.append((line.strip(), textclass))
		f.close()
	return train, test

def get_slug_data(slug): #Get data for particular category
	test = []
	train = []
	trainfile = './data/' + slug + 'train'
	testfile = './data/' + slug + 'test'
	f = open(trainfile, 'r')
	for line in f.readlines():
		train.append((line.strip(), slug))
	f.close()
	f = open (testfile, 'r')
	for line in f.readlines():
		test.append((line.strip(), slug))
	f.close()
	return train, test

def get_train_as_nparray(): #Return feature set and labels for training data
	x_train = []
	y_train = []
	trainfiles = glob.glob('./data/*train')
	for varfile in trainfiles:
		f = open(varfile, 'r')
		textclass = varfile.replace('./data/', '')
		textclass = textclass.replace('train', '')
		for line in f.readlines():
			x_train.append(line.strip())
			y_train.append([textclass])
		f.close()
	return np.array(x_train), y_train

def get_test_as_nparray(): #Return feature set and labels for test data
	x_test = []
	y_test = [] 
	testfiles = glob.glob('./data/*test')
	for varfile in testfiles:
		f = open(varfile, 'r')
		textclass = varfile.replace('./data/', '')
		textclass = textclass.replace('test', '')
		for line in f.readlines():
			x_test.append(line.strip())
			y_test.append([textclass])
		f.close()
	return np.array(x_test), y_test
