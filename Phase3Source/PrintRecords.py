import xml.etree.ElementTree as ET
import textwrap

class PrintTweets:

    @staticmethod
    def extractTweet(item):
        """ extract tweets and user info from tweet record (xml)
            values:
                tweet: id, created_at, text, retweet_count, user 
                user: name, location, description, url """

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
        """ this project's version of pprint """

        (tweet, user) = PrintTweets.extractTweet(item)    
        border = "    --------------------------------------"
        dedented_text = textwrap.dedent(tweet["text"])
        _dedented_text = textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
        print(border)
        print("    {0}".format(_dedented_text))
        print("\t---\n\ttweet id: {0}\n\tdate    : {1}\n\tretweets: {2}" \
                .format(tweet["id"], tweet["created_at"], tweet["retweet_count"]))
        print("\t---\n\tname: {0}\n\tloc : {1}\n\tdes : {2}\n\turl : {3}" \
                .format(user["name"], user["location"], user["description"], user["url"]))

        