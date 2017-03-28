class QueryComponent:
	"""A component of a query as contained in a Query object"""

	def __init__(self, value, operator):
		"""
		Arguments:
		value -- the value (term or date) (eg. "german" or "2011/01/01")
		operator -- the QueryOperator
		"""

		self._value = value
		self._operator = operator

	def __eq__(self, other):

		if not isinstance(other, QueryComponent): return False
		return self._value == other.value and self._operator == other.operator

	@property
	def value(self):

		return self._value

	@property
	def operator(self):

		return self._operator