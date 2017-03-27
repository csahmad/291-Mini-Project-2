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

		datesIndex = OUTPUT_FOLDER + "da.idx"
		datesDatabase = db.DB()
		datesDatabase.open(datesIndex, db.DB_HASH, db.DB_CREATE)
		datesCursor = datesDatabase.cursor()

		firstIndex = tweetsCursor.first()
		firstTweet = firstIndex[1]
		firstTweetLocation = firstIndex[0]
		print(firstTweet.decode("utf-8"))
		print(firstTweetLocation.decode("utf-8"))
		date = datesDatabase.get(firstTweetLocation)
		print(date[0].decode("utf-8"))

		tweetsCursor.close()
		tweetsDatabase.close()

if __name__ == "__main__":
	Main.main()