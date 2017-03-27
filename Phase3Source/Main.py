from bsddb3 import db

OUTPUT_FOLDER = "../Output/"

class Main:
	"""Run the program"""

	@staticmethod
	def main():
		"""Run the program"""

		tweetsIndex = OUTPUT_FOLDER + "tw.idx"
		tweetsDatabase = db.DB()
		tweetsDatabase.open(tweetsIndex, db.DB_HASH, db.DB_CREATE)
		tweetsCursor = tweetsDatabase.cursor()

		firstIndex = tweetsCursor.first()
		print(firstIndex)
		#firstTweet = I

		tweetsCursor.close()
		tweetsDatabase.close()

if __name__ == "__main__":
	Main.main()