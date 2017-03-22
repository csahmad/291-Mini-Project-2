TWEET_INDEX = "tw.idx"
TERMS_INDEX = "te.idx"
DATES_INDEX = "da.idx"

class Main:
	"""Run the program"""

	@staticmethod
	def main():
		"""Run the program"""

		Main.makeTweetsIndex
		Main.makeTermsIndex
		Main.makeDatesIndex

	@staticmethod
	def makeTweetsIndex():
		"""Make the index for tweets.txt"""

		pass

	@staticmethod
	def makeTermsIndex():
		"""Make the index for terms.txt"""

		pass

	@staticmethod
	def makeDatesIndex():
		"""Make the index for dates.txt"""

		pass

	@staticmethod
	def getKeyData(string):
		"""
		Given a string with a key and the corresponding data in the form
		"key:data", convert the data into a form db_load works with and return
		a tuple in the form (key, data)
		"""

		string = Main.convertSpecialCharacters(string)
		colonIndex = string.index(":")
		key = string[:colonIndex]
		data = string[colonIndex + 1:]
		return (key, data)

	@staticmethod
	def convertSpecialCharacters(string):
		"""
		Convert special characters in the given string to a form db_load works
		with
		"""

		return string.replace("\\", "&92;")

if __name__ == "__main__":
	Main.main()