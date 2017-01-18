import unittest
from main.main import prime_num


def test_dividible_one(self):
	"""
		Testing didvisibility by one
		"""
	self.assertEqual(self.prime_num(6), 6)

def test_divisible_itself(self):
	"""
	Testing divisibility by itself
		"""
	self.assertEqual(self.prime_num(4), 1)

def test_list(self):
	"""If input is a list
		"""
	self.assertIsinstance(self.prime_num(i, list))

def test_is_string(self):
	"""
	If number is string in order to loop
		"""
	self.assertTrue(self.prime_num('7'))

if __name__ == '__main__':
	unittest.main()