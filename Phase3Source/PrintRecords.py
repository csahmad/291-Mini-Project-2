import xml.etree.ElementTree as ET


class PrintTweets:

    @staticmethod
    def extractTweet(item):
        """
            tweet: id, created_at, text, retweet_count, user 
            user: name, location, description, url
        """

        root = ET.fromstring(item)
        tweet = {}
        user = {}
        for child in root:
            if child.tag != "user":
                tweet[child.tag] = child.text
            else:
                for grandchild in child:
                    user[grandchild.tag] = grandchild.text

        return tweet, user
        
    @staticmethod
    def prettyprint(item):
        (tweet, user) = PrintTweets.extractTweet(item)    
        border = "--------------------------------------"
        print(border)
        print("{0}".format(tweet["text"]))
        print(" ---\n tweet id: {0}\n date    : {1}\n retweets: {2}" \
                .format(tweet["id"], tweet["created_at"], tweet["retweet_count"]))
        print(" ---\n name: {0}\n loc : {1}\n des : {2}\n url : {3}" \
                .format(user["name"], user["location"], user["description"], user["url"]))

        