import sys
import xml.etree.ElementTree as etree
"""
You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.
The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is 1+1+3 = 5
"""


c = 0 
def get_attr_number(node):
    global c
    c += len(node.attrib)
    for i in node:
        if len(i) > 0:
            c += len(i.attrib)
            get_attr_number(i)
        else:
            c += len(i.attrib) 
    return c 

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
