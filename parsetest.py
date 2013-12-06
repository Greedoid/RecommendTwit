import unittest
import sys
from parser import *

class TestParser (unittest.TestCase):

	def setUp(self):
		self.parser = Parser([])
	
	def test_html_strip(self):
		test_string = self.parser.strip_html('This is the best http://www.google.com code ever!')
		self.assertEqual(test_string, 'This is the best')
	
	def test_replace_ands(self):
		test_string = self.parser.replace_ands('Ed, Edd, &amp; Eddy')
		self.assertEqual(test_string, 'Ed, Edd, and Eddy')

if __name__ == '__main__':
	unittest.main()



