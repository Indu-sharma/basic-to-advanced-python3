import pytest
import sys,os
sys.path.append(os.getcwd())
from src.linked_list import *

""" 
Create the LinkedLists so you can use in your all tests. 
"""


@pytest.fixture(scope='module', autouse=True)
def createlinklists():
    mylinklist1 = LinkedList(Node(1))
    mylinklist2 = LinkedList(Node(1))
    for i in [1, 2, 3, 4]:
        mylinklist1.insert(i)

    for i in [1, 2, 3, 4]:
        mylinklist2.insert(i)
    return mylinklist1, mylinklist2
