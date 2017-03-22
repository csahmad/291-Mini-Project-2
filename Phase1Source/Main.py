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
            Main.writeTermToFile(file,"t",i,tid)

    @staticmethod
    def writeTermToFile(file, intype, string, tid):
        """writes the name or the location to file"""
        m = re.sub('[^0-9a-zA-Z_]','', string)
        if m != None:
            if len(m) > 2:
                file.write('{0}-{1}:{2}\r\n'.format(intype,m.lower(),tid))

    @staticmethod
    def writeToFile(file, string, tid):
        """writes the whole tweet or the date and writes it to file"""
        file.write('{0}:{1}\r\n'.format(string,tid))

    @staticmethod
    def xmlParser(fterms, fdates, ftweets, line):
        """parses each status in the xml file"""        
        root = ET.fromstring(line)
        # print(root.tag)
        for child in root:
            # f = open ('terms.txt')
            if child.tag == "id":
                tid = child.text

            if child.tag == "text":
                Main.writeToFile(ftweets, child.text, tid)
                parsedText = Main.readText(child.text)
                Main.writeTermsToFile(fterms, parsedText, tid)

            if child.tag == "user":
                for grandchild in child:
                    if grandchild.tag == "name":
                        Main.writeTermToFile(fterms,"n", grandchild.text, tid)
                    if grandchild.tag == "location":
                        Main.writeTermToFile(fterms,"l", grandchild.text, tid)
            
            if child.tag == "created_at":
                Main.writeToFile(fdates, child.text, tid)

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
