class Query:
	"""Represents a (parsed) query"""

	def __init__(self, terms, dates):
		"""
		Arguments:
		exactTerms -- exact terms (ignoring case) as a list of QueryComponent
			objects
		startsWith -- term prefixes as a list of QueryComponent objects
		dates -- dates as a list of QueryComponent objects
		"""

		self._terms = terms
		self._dates = dates

	def __eq__(self, other):

		if not isinstance(other, Query): return False
		return self._terms == other.terms and self._dates == other.dates

	@property
	def terms(self):

		return self._terms

	@property
	def dates(self):

		return self._dates