import xml.etree.ElementTree as ET
import sys
from bsddb3 import db
from Interface import *
from QueryOperator import *

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
    def searchTweets(ids, database):
        """search for tweets from a list of tweet ids"""
        tweets = []
        for i in ids:
            tweets.append(database.get(str.encode(i.strip())))
        return tweets          

    @staticmethod
    def searchTerms(key, cur, isCheckAll):
        """search for eact terms"""
        ids = []
        iter = cur.first()

        if isCheckAll == False:
            while iter:
                if iter[0].decode("utf-8") == key:
                    break
                iter = cur.next()
            
            if iter != None:
                while iter:
                    if iter[0].decode("utf-8") != key:
                        break
                    ids.append(iter[1].decode("utf-8"))
                    iter = cur.next()
        else:
            while iter:
                if iter[0].decode("utf-8").endswith(key, 2, len(iter[0].decode("utf-8"))):
                    break
                iter = cur.next()

            if iter != None:
                while iter:
                    if iter[0].decode("utf-8").endswith(key, 2, len(iter[0].decode("utf-8"))) == False:
                        break
                    ids.append(iter[1].decode("utf-8"))
                    iter = cur.next()
            
        return ids

    @staticmethod
    def searchTermsWC(key, cur, isCheckAll):
        """search for wildcard terms"""
        ids = []
        iter = cur.first()

        if isCheckAll == False:
            while iter:
                if iter[0].decode("utf-8").startswith(key):
                    break
                iter = cur.next()
            
            if iter != None:
                while iter[0].decode("utf-8").startswith(key):
                    ids.append(iter[1].decode("utf-8"))
                    iter = cur.next()

        else:
            while iter:
                if iter[0].decode("utf-8").endswith(key, 2, len(key)+2):
                    break
                iter = cur.next()

            if iter != None:
                while iter:
                    if iter[0].decode("utf-8").endswith(key, 2, len(key)+2) == False:
                        break
                    ids.append(iter[1].decode("utf-8"))
                    iter = cur.next()
                

        return ids

    @staticmethod
    def searchDates(date, cur, operator):
        ids = []

        if operator == QueryOperator.GREATER_THAN:
            iter = cur.set_range(str.encode(date))
            bound = cur.set_range(str.encode(date))
            while iter:
                if iter[0].decode("utf-8") != bound[0].decode("utf-8"):
                    ids.append(iter[1].decode("utf-8"))
                iter = cur.next()

        elif operator == QueryOperator.LESS_THAN:
            bound = cur.set_range(str.encode(date))
            iter = cur.first()
           
            while iter:
                if iter[0] == bound[0]:
                    break
                ids.append(iter[1].decode("utf-8"))
                iter = cur.next()

        elif operator == QueryOperator.EQUALS:
            ids = Main.searchTerms(date, cur, False)

        return ids
            
    @staticmethod
    def prettyprint(item):
        root = ET.fromstring(item)
        print("")
        for child in root:
            if child.tag != "user":
                if child.text != None: print(child.tag + ": " + child.text)
            else:
                print(child.tag + ": " + child.text)
                for grandchild in child:
                    if grandchild.text != None: print("  " + grandchild.tag + ": " + grandchild.text)
        print("------------------------\n")
        

    @staticmethod
    def main():
        """ Run the program """

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
                
                if i.isExactMatch == True: ids = Main.searchTerms(key, te_cur, isCheckAll)
                else: ids = Main.searchTermsWC(key, te_cur, isCheckAll)

                tweets = Main.searchTweets(ids, tw_db)
                allTweets.append(set(tweets))

        if dates != []:
            for i in dates:
                print(i.operator)
                ids = Main.searchDates(i.value, da_cur, i.operator)
                tweets = Main.searchTweets(ids, tw_db)
                allTweets.append(set(tweets))
        
        finalSet = allTweets[0]
        for i in range(len(allTweets)-1):
            finalSet = finalSet.intersection(allTweets[i+1])

        for i in finalSet:
            Main.prettyprint(i)

        ### close connections
        Main.closeConnection(te_db, te_cur)
        Main.closeConnection(da_db, da_cur)
        Main.closeConnection(tw_db, tw_cur)

if __name__ == "__main__":
    while True:
        try:
            Main.main()
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print('\n\nBYE!\n')
            sys.exit(0)