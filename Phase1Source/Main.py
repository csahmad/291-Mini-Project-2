import xml.etree.ElementTree as ET

class Main:
    """Run the program"""
    @staticmethod
    def xmlParser():
        data = {}
        with open('10.txt') as f:
            for line in f:
                print(line)
                if line.startswith("<status>"):
                    root = ET.fromstring(line)
                    # print(root.tag)
                    for child in root:
                        print(child.tag, child.text)
                        
                print("\n")

    @staticmethod
    def main():
        """Run the program"""
        Main.xmlParser()

if __name__ == "__main__":
	Main.main()
