import sys
import re

class Parser:
	def __init__(self, twitObj):
		self.obj = twitObj
	
	def get_text(self, num):
		raw = (self.obj[num].text).encode('ascii', 'ignore')
		return self.parsed_string(raw)
	
	def get_max_id(self): #Gets the max ID in the set, used for iterating through API calls
		max_id = 0
		for tweet in self.obj:
			if tweet.id > max_id:
				max_id = tweet.id
		return max_id
	
	def get_min_id(self): #This actually gets passed into the rest call
		min_id = self.get_max_id()
		for tweet in self.obj:
			if tweet.id < min_id:
				min_id = tweet.id
		return min_id

	def strip_html(self, raw): #Matches against the regex - removes links 
		p = re.compile(r'( |)(h|H)ttp.*( |\Z)', re.DOTALL)
		text = re.sub(p, '', raw)
		return text
	
	def replace_ands(self, raw): #Matches against the regex - turns the amp; character into 'and'
		p = re.compile(r'&amp;', re.DOTALL)
		text = re.sub(p, 'and', raw)
		return text


	def parsed_string(self, raw): #Overall method to be called when gettign text - made this way so I can add more in case need to parse more
		clean = self.strip_html(raw)
		clean = self.replace_ands(clean)
		return clean.lower()
