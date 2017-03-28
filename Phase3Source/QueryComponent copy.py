class QueryComponent:
	"""A component of a query as contained in a Query object"""

	def __init__(self, value, operator):

		self._value = value
		self._operator = operator

	@property
	def value(self):

		return self._value

	@property
	def operator(self):

		return self._operator