import xml.etree.ElementTree as ET
import sys
import os
import fileinput

class Main:
    """Run the program"""

    @staticmethod
    def readText(text):
        return text.split()
    
    @staticmethod
    def writeTermToFile(file, terms, tid):
        for i in terms:
            file.write('t-{0}:{1}\r\n'.format(i.lower(),tid))

    @staticmethod
    def writeUNameToFile(file, uname, tid):
        file.write('n-{0}:{1}\r\n'.format(uname,tid))

    @staticmethod
    def writeULocationToFile(file, ulocation, tid):
        file.write('l-{0}:{1}\r\n'.format(ulocation,tid))

    @staticmethod
    def xmlParser(file, line):
        root = ET.fromstring(line)
        # print(root.tag)
        for child in root:
            # f = open ('terms.txt')
            if child.tag == "id":
                tid = child.text
            if child.tag == "text":
                parsedText = Main.readText(child.text)
                Main.writeTermToFile(file, parsedText, tid)
            if child.tag == "user":
                for grandchild in child:
                    if grandchild.tag == "name":
                        Main.writeUNameToFile(file, grandchild.text, tid)
                    if grandchild.tag == "location":
                        Main.writeULocationToFile(file, grandchild.text, tid)

            print(child.tag, child.text)

    @staticmethod
    def main():
        """Run the program"""
        f = open('../Output/terms.txt', 'w')

        for line in fileinput.input():
            if line.startswith("<status>"):
                print(line)
                Main.xmlParser(f, line)
        f.close()

if __name__ == "__main__":
	Main.main()
