from QueryOperator import QueryOperator

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

	def __str__(self):

		if self._operator == QueryOperator.EQUALS:
			operator = ":"

		elif self._operator == QueryOperator.LESS_THAN:
			operator = "<"

		elif self._operator == QueryOperator.GREATER_THAN:
			operator = ">"

		else:
			raise RuntimeError("I should not be here.")

		return operator + self._value

	def __eq__(self, other):

		if not isinstance(other, QueryComponent): return False
		return self._value == other.value and self._operator == other.operator

	@property
	def value(self):

		return self._value

	@property
	def operator(self):

		return self._operator