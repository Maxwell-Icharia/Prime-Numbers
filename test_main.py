import unittest, main



class TestPrimes(unittest.TestCase):
	
	def test_dividible_one(self):
		"""
		Testing didvisibility by one
			"""
		self.assertEqual(main.div_one(8, 1), 8)
	
	def test_divisible_itself(self):
		"""
		Testing divisibility by itself
			"""
		self.assertEqual(main.div_self(5), 1)

	def test_list(self):
		"""If input is a list
			"""
		self.Isinstance(main.is_list(i, list))

	def test_is_string(self):
		"""
		If number is string in order to loop
			"""
		self.assertTrue(main.is_string('7'))