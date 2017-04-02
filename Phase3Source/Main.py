from bsddb3 import db
from Interface import Interface
from SearchDates import SearchDates
from SearchTerms import SearchTerms
from SearchTweets import SearchTweets
from PrintRecords import PrintTweets

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
        """ ends cursor and database connection """
        database.close()
        cursor.close()


    @staticmethod
    def getInput():
        """ fetch the input from user 
            returns a list of parsed terms and dates
        """
        query = Interface.readAndParse()
        return query.terms, query.dates
            

    @staticmethod
    def main():
        """ Run the program """

        """ start connections and get cursor an databases """
        (te_db, te_cur) = Main.startConnection(OUTPUT_FOLDER + "te.idx")
        (da_db, da_cur) = Main.startConnection(OUTPUT_FOLDER + "da.idx")
        (tw_db, tw_cur) = Main.startConnection(OUTPUT_FOLDER + "tw.idx")
        
        (terms, dates) = Main.getInput()

        allTweets = []

        if terms != []: 
            for i in terms:
                if i.field == "text":
                    key = "t-" + i.value
                    isCheckAll = False

                if i.field == "name":
                    key = "n-" + i.value
                    isCheckAll = False
                
                if i.field == "location":
                    key = "l-" + i.value
                    isCheckAll = False
                else:
                    key = i.value
                    isCheckAll = True
                
                if i.isExactMatch == True: ids = SearchTerms.searchTerms(key, te_cur, isCheckAll)
                else: ids = SearchTerms.searchTermsWC(key, te_cur, isCheckAll)

                tweets = SearchTweets.searchTweets(ids, tw_db)
                allTweets.append(set(tweets))

        if dates != []:
            for i in dates:
                ids = SearchDates.searchDates(i.value, da_cur, i.operator)
                tweets = SearchTweets.searchTweets(ids, tw_db)
                allTweets.append(set(tweets))
        
        finalSet = allTweets[0]
        for i in range(len(allTweets)-1):
            finalSet = finalSet.intersection(allTweets[i+1])

        for i in finalSet:
            PrintTweets.prettyprint(i)
            print("")

        """ close connections """
        Main.closeConnection(te_db, te_cur)
        Main.closeConnection(da_db, da_cur)
        Main.closeConnection(tw_db, tw_cur)

if __name__ == "__main__":
    while True:
        try:
            Main.main()
        except ValueError as e:
            print(e)