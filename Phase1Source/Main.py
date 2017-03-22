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
    def writeTermToFile(file, terms):
        for i in terms:
            file.write('t-' + i + '\r\n')

    @staticmethod
    def xmlParser(file, line):
        root = ET.fromstring(line)
        # print(root.tag)
        for child in root:
            # f = open ('terms.txt')
            if child.tag == "text":
                parsedText = Main.readText(child.text)
                Main.writeTermToFile(file, parsedText)
                print(parsedText)
            print(child.tag, child.text)

    @staticmethod
    def main():
        """Run the program"""
        f = open('../Output/terms.txt', 'w')

        for line in fileinput.input():
            if line.startswith("<status>"):
                print(line)
                Main.xmlParser(f, line)

if __name__ == "__main__":
	Main.main()
