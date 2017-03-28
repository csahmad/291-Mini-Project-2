import re

from Query import Query
from QueryComponent import QueryComponent
from QueryOperator import QueryOperator

class QueryParser:
	"""Parses queries"""

	_SEPARATOR = "\s+"

	_EQUALS = ":"
	_LESS_THAN = "<"
	_GREATER_THAN = ">"

	_OPERATORS = (_EQUALS, _LESS_THAN, _GREATER_THAN)

	_OPERATOR = "|".join(_OPERATORS)

	_TERM = "text"
	_DATE = "date"

	_WILDCARD = "%"

	@staticmethod
	def parse(queryString):
		"""
		Return the parsed query as a Query object

		Arguments:
		queryString -- the query string to be parsed
		"""

		componentStrings = re.split(QueryParser._SEPARATOR, queryString)
		exactTerms = []
		startsWith = []
		dates = []

		for string in componentStrings:
			QueryParser._addComponent(string, exactTerms, startsWith, dates)

		return Query(exactTerms, startsWith, dates)

	@staticmethod
	def _addComponent(componentString, exactTerms, startsWith, dates):
		"""
		Add a QueryComponent (parsed from componentString) to the appropriate
		list (exactTerms, startsWith, or dates)
		"""

		match = re.search(QueryParser._OPERATOR, string)

		if match is None:

			raise ValueError('Missing operator ({0}) in "{1}"'.format(
				",".join(QueryParser._OPERATORS), string))

		operatorString = match.group()
		kind = componentString[:match.start()].lower()
		value = componentString[match.end():].lower()

		if operatorString == QueryParser._EQUALS:
			operator = QueryOperator.EQUALS

		elif operatorString == QueryParser._LESS_THAN:
			operator = QueryOperator._LESS_THAN

		elif operatorString == QueryParser._GREATER_THAN:
			operator = QueryOperator._GREATER_THAN

		else:
			raise RuntimeError("I should not be here.")

		if kind == QueryParser._TERM:

			if QueryParser._hasWildcard(value):
				value = QueryParser._removeWildcard(value)
				startsWith.append(QueryComponent(value, operator))

			else:
				exactTerms.append(QueryComponent(value, operator))

		elif kind == QueryParser._DATE:
			dates.append(QueryComponent(value, operator))

		else:
			raise ValueError('"{0}" is not valid.'.format(kind))

	@staticmethod
	def _hasWildcard(value):
		"""
		Returns whether the given value has a wildcard
		"""

		count = value.count(QueryParser._WILDCARD)

		if count > 1:

			raise ValueError(
				'Cannot have more than one wildcard ("{0}").'.format(
					QueryParser._WILDCARD))

		elif count == 1:

			if not value.endsWith(QueryParser._WILDCARD):

				raise ValueError(
					'Wildcard ("{0}") can only appear at end.'.format(
						QueryParser._WILDCARD))

			return True

		return False