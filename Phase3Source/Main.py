from bsddb3 import db
from Interface import *

OUTPUT_FOLDER = "../Output/"

class Main:
    """Run the program"""

    @staticmethod
    def startConnection(idx):
        """returns the database and cursor"""
        database = db.DB()
        database.open(idx)
        cur = database.cursor()
        return database, cur

    @staticmethod
    def closeConnection(database, cursor):
        database.close()
        cursor.close()
        
    @staticmethod
    def getInput():
        query = Interface.readAndParse()
        return query.terms, query.dates

    @staticmethod
    def main():
        """Run the program"""
        (te_db, te_cur) = Main.startConnection(OUTPUT_FOLDER + "te.idx")
        (da_db, da_cur) = Main.startConnection(OUTPUT_FOLDER + "da.idx")
        (tw_db, tw_cur) = Main.startConnection(OUTPUT_FOLDER + "tw.idx")

        (terms, dates) = Main.getInput()

        for i in terms:
            if i.field == "text":
                key = "t-" + i.value.lower()

            if i.field == "name":
                key = "n-" + i.value.lower()
            
            if i.field == "location":
                key = "l-" + i.value.lower()
                
            print(key)

            firstIndex = twe_cur.first()
            firstTweet = firstIndex[1]
            firstTweetLocation = firstIndex[0]
            print(firstTweet.decode("utf-8"))
            print(firstTweetLocation.decode("utf-8"))

        Main.closeConnection(te_db, te_cur)
        Main.closeConnection(da_db, da_cur)
        Main.closeConnection(tw_db, tw_cur)

if __name__ == "__main__":
    Main.main()
