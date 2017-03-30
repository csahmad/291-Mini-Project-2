import re

from Query import Query
from QueryComponent import QueryComponent
from QueryOperator import QueryOperator
from StringFormat import StringFormat

class QueryParser:
	"""Parses queries"""

	_SEPARATOR = "\s+"

	_EQUALS = ":"
	_LESS_THAN = "<"
	_GREATER_THAN = ">"

	_OPERATORS = (_EQUALS, _LESS_THAN, _GREATER_THAN)

	_OPERATOR = "|".join(_OPERATORS)

	_TERMS = ["text", "name", "location"]
	_DATE = "date"

	_WILDCARD = "%"

	_DATE_SEPARATOR = "/"
	_YEAR_INDEX = 0
	_MONTH_INDEX = 1
	_DAY_INDEX = 2

	@staticmethod
	def parse(queryString):
		"""
		Return the parsed query as a Query object

		Arguments:
		queryString -- the query string to be parsed
		"""

		queryString = queryString.strip()

		if queryString == "":
			raise ValueError("Query cannot be empty.")

		componentStrings = re.split(QueryParser._SEPARATOR, queryString)
		terms = []
		dates = []

		for string in componentStrings:
			QueryParser._addComponent(string, terms, dates)

		return Query(terms, dates)

	@staticmethod
	def _addComponent(componentString, terms, dates):
		"""
		Add a QueryComponent (parsed from componentString) to the appropriate
		list (terms or dates)
		"""

		match = re.search(QueryParser._OPERATOR, componentString)

		if match is None:

			raise ValueError('Missing operator ({0}) in "{1}"'.format(
				", ".join(QueryParser._OPERATORS), componentString))

		operatorString = match.group()
		kind = componentString[:match.start()].lower()
		value = componentString[match.end():].lower()

		if operatorString == QueryParser._EQUALS:
			operator = QueryOperator.EQUALS

		elif operatorString == QueryParser._LESS_THAN:
			operator = QueryOperator.LESS_THAN

		elif operatorString == QueryParser._GREATER_THAN:
			operator = QueryOperator.GREATER_THAN

		else:
			raise RuntimeError("I should not be here.")

		if kind in QueryParser._TERMS:

			if QueryParser._hasWildcard(value):
				value = QueryParser._removeWildcard(value)
				terms.append(QueryComponent(kind, value, operator, False))

			else:
				terms.append(QueryComponent(kind, value, operator))

		elif kind == QueryParser._DATE:
			QueryParser._validateDate(value)
			dates.append(QueryComponent(kind, value, operator))

		else:
			raise ValueError('"{0}" is not valid.'.format(kind))

	@staticmethod
	def _removeWildcard(value):
		"""Remove the wildcard and return the result"""

		return value[:-len(QueryParser._WILDCARD)]

	@staticmethod
	def _validateDate(dateString):
		"""Raise an error if the given date is not in the correct format"""

		split = dateString.split(QueryParser._DATE_SEPARATOR)

		if len(split) != 3:

			raise ValueError('Date must be in format "{0}".'.format(
				QueryParser._getDateFormat()))

		for component in split:

			if not StringFormat.isPositiveInt(component):
				raise ValueError("A date must consist of positive integers.")

		yearString = split[QueryParser._YEAR_INDEX]
		monthString = split[QueryParser._MONTH_INDEX]
		month = int(monthString)
		dayString = split[QueryParser._DAY_INDEX]
		day = int(dayString)

		if len(yearString) != 4:
			raise ValueError("Year must be four characters long.")

		if len(monthString) != 2:
			raise ValueError("Month must be two characters long.")

		if len(dayString) != 2:
			raise ValueError("Day must be two characters long.")

		if month == 0:
			raise ValueError("Month cannot be 0.")

		if day == 0:
			raise ValueError("Day cannot be 0.")

		if month > 12:
			raise ValueError("Month cannot be over 12.")

		if day > 31:
			raise ValueError("Day cannot be over 31.")

	@staticmethod
	def _getDateFormat():
		"""Return a string representation of the expected format of dates"""

		components = [None, None, None]
		components[QueryParser._YEAR_INDEX] = "yyyy"
		components[QueryParser._MONTH_INDEX] = "MM"
		components[QueryParser._DAY_INDEX] = "dd"
		return QueryParser._DATE_SEPARATOR.join(components)

	@staticmethod
	def _hasWildcard(value):
		"""Returns whether the given value has a wildcard"""

		count = value.count(QueryParser._WILDCARD)

		if count > 1:

			raise ValueError(
				'Cannot have more than one wildcard ("{0}").'.format(
					QueryParser._WILDCARD))

		elif count == 1:

			if not value.endswith(QueryParser._WILDCARD):

				raise ValueError(
					'Wildcard ("{0}") can only appear at end.'.format(
						QueryParser._WILDCARD))

			return True

		return False