import xml.etree.ElementTree as ET
import sys
import os

class Main:
    """Run the program"""

    @staticmethod
    def readText(text):
        return text.split()
    
    @staticmethod
    def writeTermToFile(file, terms, tid):
        for i in terms:
            if len(i) > 2:
                file.write('t-{0}:{1}\r\n'.format(i.lower(),tid))

    @staticmethod
    def writeUNameToFile(file, uname, tid):
        file.write('n-{0}:{1}\r\n'.format(uname.lower(),tid))

    @staticmethod
    def writeULocationToFile(file, ulocation, tid):
        file.write('l-{0}:{1}\r\n'.format(ulocation.lower(),tid))

    @staticmethod
    def writeDateToFile(file, date, tid):
        file.write('{0}:{1}\r\n'.format(date,tid))

    @staticmethod
    def writeTweetToFile(file, tweet, tid):
        file.write('{0}:{1}\r\n'.format(tid,tweet))

    @staticmethod
    def xmlParser(fterms, fdates, ftweets, line):
        root = ET.fromstring(line)
        # print(root.tag)
        for child in root:
            # f = open ('terms.txt')
            if child.tag == "id":
                tid = child.text
            if child.tag == "text":
                Main.writeTweetToFile(ftweets, child.text, tid)
                parsedText = Main.readText(child.text)
                Main.writeTermToFile(fterms, parsedText, tid)
            if child.tag == "user":
                for grandchild in child:
                    if grandchild.tag == "name":
                        Main.writeUNameToFile(fterms, grandchild.text, tid)
                    if grandchild.tag == "location":
                        Main.writeULocationToFile(fterms, grandchild.text, tid)
            
            if child.tag == "created_at":
                Main.writeDateToFile(fdates, child.text, tid)

            print(child.tag, child.text)

    @staticmethod
    def main():
        """Run the program"""
        f1 = open('../Output/terms.txt', 'w')
        f2 = open('../Output/dates.txt', 'w')
        f3 = open('../Output/tweets.txt', 'w')
        

        for line in sys.stdin:
            if line.startswith("<status>"):
                print(line)
                Main.xmlParser(f1, f2, f3, line)

        f1.close()
        f2.close()
        f3.close()

if __name__ == "__main__":
	Main.main()
