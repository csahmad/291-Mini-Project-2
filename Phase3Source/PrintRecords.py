import xml.etree.ElementTree as ET

class PrintRecords:
    
    @staticmethod
    def prettyprint(item):
        """ this project's version of pprint
            prints the tweet record nicely
        """
        root = ET.fromstring(item)
        print("")
        for child in root:
            if child.tag != "user":
                if child.text != None: 
                    if child.tag == "id" or child.tag == "text":
                        print(child.tag + ": \t\t" + child.text)
                    else:
                        print(child.tag + ": \t" + child.text)
            else:
                # print(child.tag + ": " + child.text)
                for grandchild in child:
                    if grandchild.text != None: print("user " + grandchild.tag + ": \t" + grandchild.text)
        print("------------------------\n")