def prime_num(b):
	"""Main Prime number function
		"""
	for i in xrange(b):
		if i >= 2:	
			if (i % 1 == i) & (i % i == 1):
				return i + 'Is Prime number'
			else:
				return 'Not Prime number'