import unittest
import sys
import os
sys.path.append(os.path.join('..', 'actors'))
import parser as Parser
import suggestions as DB

class TestParser (unittest.TestCase):

	def set_up(self):
		self.parser = Parser(dummy)
	
	def test_html_strip(self):
		test_string = self.thisparser.strip_html('This is the best http://www.google.com code ever!')
		self.assertEqual(test_string, 'This is the best code ever!')
	
	def test_replace_ands(self):
		test_string = self.parser.replace_ands('Ed, Edd, &amp; Eddy')
		self.assertEqual(test_string, 'Ed, Edd, and Eddy')
	
	def test_add_suggestion(self):
		DB.add_suggestion('test', 123)
		self.assertEqual(DB.check_if_exists('test'), true)

	def test_get_level(self):
		self.assertEqual(DB.get_reading_level('test'), 123)

	def test_addition_test(self):
		var = 'hello' 
		self.assertEqual(var, 'hello')

if __name__ == '__main__':
	unittest.main()



