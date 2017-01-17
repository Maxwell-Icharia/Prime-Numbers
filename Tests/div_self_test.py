import unittest

class Div_Self(unittest.TestCase):

	def test_divisible_itself(self):
		"""
		Testing divisibility by itself
			"""
		self.assertEqual(div_self(5), 1)

if __name__ == '__main__':
	unittest.main()