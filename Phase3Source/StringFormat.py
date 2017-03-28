class StringFormat:
	"""Check the format of a string"""

	@staticmethod
	def isPositiveInt(string):
		"""
		Return whether the string is a positive integer

		'0' returns True
		"""

		try:
			integer = int(string)
			return integer >= 0

		except ValueError:
			return False