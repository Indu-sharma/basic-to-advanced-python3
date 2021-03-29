"""
Adding elements to Doubly LinkedList from the Beginning and Traversing elements from the backwards
makes a Queue. However, If traverse is done from forward, makes it a Stack.

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createDll(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def insert_start(self, value):
        if self.head:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.createDll(value)

    def delete_start(self):

        if self.head:
            to_del = self.head
            i = self.head.next
            i.prev= None
            self.head = i
            print(f'Element {to_del.value} is deleted from start of Doubly LinkedList')

    def __iter__(self):
        """
        This makes LinkedList an Iterable; Here we will traverse Backwards.
        """
        i = self.tail
        while i is not None:
            yield i.value
            i = i.prev

    def __str__(self):
        return '<->'.join([str(i) for i in self])


if __name__ == '__main__':
    """
    OutPut:
    DoublyLinkedList traversed from backwards:(Queue-like)
    100<->10<->20<->30
    Element 30 is deleted from start of Doubly LinkedList
    100<->10<->20
    """
    doubly = DoublyLinkedList()
    doubly.createDll(100)
    # Insert Values to the LinkedList at the beginning.
    doubly.insert_start(10)
    doubly.insert_start(20)
    doubly.insert_start(30)
    print('DoublyLinkedList traversed from backwards:(Queue-like)')
    print(doubly)
    doubly.delete_start()
    print(doubly)
