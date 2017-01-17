import unittest, Main.is_string
from Main.is_string import is_string


class IsPrime(unittest.TestCase):

	def test_is_string(self):
		"""
		If number is string in order to loop
			"""
		self.assertTrue(is_string('7'))

if __name__ == '__main__':
	unittest.main()