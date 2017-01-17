import unittest


class DivOne(unittest.TestCase):
	
	def test_dividible_one(self):
		"""
		Testing didvisibility by one
			"""
		self.assertEqual(div_one(8, 1), 8)
	
if __name__ == '__main__':
	unittest.main()