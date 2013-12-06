import glob
import numpy as np

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
		f = open(varfile, 'rU')
		textclass = varfile.replace('./data/', '')
		textclass = textclass.replace('test', '')
		for line in f.readlines():
			x_test.append(line.strip())
			y_test.append([textclass])
		f.close()
	return np.array(x_test), y_test

def get_test_as_nparray(slug): #Does what is says - useful for testing effectiveness of classifeir
	x_test = []
	y_test = []
	testfile = './data/' + slug + 'test'
	f = open(testfile, 'rU')
	for line in f.readlines():
		x_test.append(line.strip())
		y_test.append([slug])
	f.close()
	return np.array(x_test), y_test
