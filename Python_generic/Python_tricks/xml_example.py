import sys
import xml.etree.ElementTree as etree


"""
Example -1:

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
    
    
"""
Example - 2:

You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as .

"""

import xml.etree.ElementTree as etree


maxdepth = 0
def depth(node, level): 
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for child in node:
        depth(child, level + 1) 

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)    

    
