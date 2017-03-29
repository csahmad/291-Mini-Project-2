from QueryOperator import QueryOperator

class QueryComponent:
	"""A component of a query as contained in a Query object"""

	def __init__(self, field, value, operator, isExactMatch = True):
		"""
		Arguments:
		field -- the field to search by (eg. "name")
		value -- the value (term or date) (eg. "german" or "2011/01/01")
		operator -- the QueryOperator
		isExactMatch -- whether the value represents an exact match (does not
			represent a prefix match)
		"""

		self._field = field
		self._value = value
		self._operator = operator
		self._isExactMatch = isExactMatch

	def __str__(self):

		if self._operator == QueryOperator.EQUALS:
			operator = ":"

		elif self._operator == QueryOperator.LESS_THAN:
			operator = "<"

		elif self._operator == QueryOperator.GREATER_THAN:
			operator = ">"

		else:
			raise RuntimeError("I should not be here.")

		combined = self._field + operator + self._value

		if (self._isExactMatch): return combined
		return combined + "%"

	def __eq__(self, other):

		if not isinstance(other, QueryComponent): return False

		return self._field == other.field and \
			self._value == other.value and \
			self._operator == other.operator and \
			self._isExactMatch == other.isExactMatch

	@property
	def field(self):

		return self._field

	@property
	def value(self):

		return self._value

	@property
	def operator(self):

		return self._operator

	@property
	def isExactMatch(self):

		return self._isExactMatch