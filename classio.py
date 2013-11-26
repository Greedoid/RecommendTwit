import glob

def parse_class(slug):
	test, train = []
	#testfiles = glob.glob('./data/' + slug +'test')
	for varfile in testfiles:
		f = open(varfile, 'r')
		for line in f.readlines():
			test.append(line, slug)
		f.close()
	trainfiles = glob.glob('./data/' + slug +'train')
	for varfile in trainfiles:
		f = open(varfile, 'r')
		for line in f.readlines():
			train.append(line, slug)
		f.close()
	return train, test

def get_all_data():
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

