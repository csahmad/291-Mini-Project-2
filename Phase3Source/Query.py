class Query:
	"""Represents a (parsed) query"""

	def __init__(self, exactTerms, startsWith, dates):
		"""
		Arguments:
		exactTerms -- exact terms (ignoring case) as a list of QueryComponent
			objects
		startsWith -- term prefixes as a list of QueryComponent objects
		dates -- dates as a list of QueryComponent objects
		"""

		self._exactTerms = exactTerms
		self._startsWith = startsWith
		self._dates = dates

	def __eq__(self, other):

		if not isinstance(other, Query): return False

		return self._exactTerms == other.exactTerms and \
			self._startsWith == other.startsWith and \
			self._dates == other.dates

	@property
	def exactTerms(self):

		return self._exactTerms

	@property
	def startsWith(self):

		return self._startsWith

	@property
	def dates(self):

		return self._dates