import unittest
import sys
from suggestions import *

class TestParser (unittest.TestCase):

	def test_add_suggestion(self):
		add_suggestion('test', 'clowning')
		self.assertTrue(check_if_exists('test'))
		remove_suggestion('test')
	
	def test_get_suggestion(self):
		suggestions = get_suggestions('science')
		self.assertTrue(len(suggestions) <= 5)

if __name__ == '__main__':
	unittest.main()



