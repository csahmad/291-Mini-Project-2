from QueryParser import QueryParser
import sys

class Interface:
	"""The terminal interface"""

	_PROMPT = "Query: "

	@staticmethod
	def readAndParse():
		"""
		Prompt the user for a query and return the parsed query as a Query
		"""
		print("\ntype 'exit' to leave program")
		inputString = input(Interface._PROMPT)
		if inputString.lower().strip() == "exit":
    			print("BYE!\n")
    			sys.exit(0)
		else:
    			return QueryParser.parse(inputString)