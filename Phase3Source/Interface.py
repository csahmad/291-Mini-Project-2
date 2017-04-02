from QueryParser import QueryParser

class Interface:
	"""The terminal interface"""

	_PROMPT = "Query: "

	@staticmethod
	def readAndParse():
		"""
		Prompt the user for a query and return the parsed query as a Query
		"""
		return QueryParser.parse(input(Interface._PROMPT))