import xml.etree.ElementTree as ET
import sys
import os
import re

class Main:
    """Run the program"""

    @staticmethod
    def readText(text):
        """reads the tweet text and return terms as a list"""
        return text.split()
    
    @staticmethod
    def writeTermsToFile(file, terms, tid):
        """reads a list and writes each item to a file"""
        for i in terms:
            Main.writeToFile1(file,"t",i,tid)

    @staticmethod
    def writeToFile1(file, intype, arg1, arg2):
        """ writes to file in dash-colon format
            intype-arg1:arg2 """
        if arg1 != None:
            m = re.sub('[^0-9a-zA-Z_]+','', arg1)
            if m != None:
                if len(m) > 2:
                    file.write('{0}-{1}:{2}\r\n'.format(intype,m.lower(),arg2))

    @staticmethod
    def writeToFile2(file, arg1, arg2):
        """ writes to file in colon format
            arg1 : arg2 """
        file.write('{0}:{1}\r\n'.format(arg1,arg2))

    @staticmethod
    def xmlParser(fterms, fdates, ftweets, line):
        """ parses each status in the xml file
            assumes each status is one line """        
        root = ET.fromstring(line)
        # print(root.tag)
        for child in root:
            # f = open ('terms.txt')
            if child.tag == "id":
                tid = child.text

            if child.tag == "text":
                Main.writeToFile2(ftweets, tid, child.text)
                parsedText = Main.readText(child.text)
                Main.writeTermsToFile(fterms, parsedText, tid)

            if child.tag == "user":
                for grandchild in child:
                    if grandchild.tag == "name":
                        Main.writeToFile1(fterms,"n", grandchild.text, tid)
                    if grandchild.tag == "location":
                        Main.writeToFile1(fterms,"l", grandchild.text, tid)
            
            if child.tag == "created_at":
                Main.writeToFile2(fdates, child.text, tid)

            # print(child.tag, child.text)

    @staticmethod
    def main():
        """Run the program"""
        f1 = open('../Output/terms.txt', 'w')
        f2 = open('../Output/dates.txt', 'w')
        f3 = open('../Output/tweets.txt', 'w')
        

        for line in sys.stdin:
            if line.startswith("<status>"):
                # print(line)
                Main.xmlParser(f1, f2, f3, line)

        f1.close()
        f2.close()
        f3.close()

if __name__ == "__main__":
	Main.main()
