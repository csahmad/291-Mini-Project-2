class SearchTweets:
    
    @staticmethod
    def searchTweets(ids, database):
        """ search for tweets from a list of tweet ids
            returns a list of tweets
        """
        tweets = []
        for i in ids:
            tweets.append(database.get(str.encode(i.strip())))
        return tweets