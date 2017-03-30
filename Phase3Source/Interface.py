from pprint import pprint

from QueryParser import QueryParser

class Interface:
	"""The terminal interface"""

	_PROMPT = "Query:"

	@staticmethod
	def readAndParse():
		"""
		Prompt the user for a query and return the parsed query as a Query
		"""

		try:
			return QueryParser.parse(input(Interface._PROMPT))

		except ValueError as e:
			print(e)
			return None

if __name__ == "__main__":

	query = Interface.readAndParse()

	if query is not None:
		pprint([str(component) for component in query.terms])
		pprint([str(component) for component in query.dates])