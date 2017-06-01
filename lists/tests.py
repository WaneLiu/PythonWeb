from django.test import TestCase
import unittest
class Smoketest(TestCase):
	"""docstring for Smoketest"""
	def test_bad_maths(self):
		self.assertEqual(1 + 1, 3)

	# def __init__(self, arg):
	# 	super(Smoketest, self).__init__()
	# 	self.arg = arg
		
# Create your tests here.
