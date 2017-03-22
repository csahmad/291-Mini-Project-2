import xml.etree.ElementTree as ET
import sys
import fileinput

class Main:
    """Run the program"""
    @staticmethod
    def xmlParser(line):
        if line.startswith("<status>"):
            root = ET.fromstring(line)
            # print(root.tag)
            for child in root:
                print(child.tag, child.text)
                        
        print("\n")

    @staticmethod
    def main():
        """Run the program"""
        for line in fileinput.input():
            print(line)
            Main.xmlParser(line)

if __name__ == "__main__":
	Main.main()
