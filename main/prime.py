def prime_num(n):
	"""Main Prime number function
		"""
	if n == int:
		b = str(n)
		for i in xrange(b):
			if i >= 2:	
				if (i % 1 == i) & (i % i == 1):
					return i