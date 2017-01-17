def is_string(y):
	try:
		b = str(y)
	except int as e:
		raise e