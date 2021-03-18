class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class DublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.my_list = []

    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.tail = new_node

    def __iter__(self):
        """
        This makes Circular LinkedList an Iterable.
        """
        i = self.head
        while i:
            yield i.value
            if i.next is self.head:
                break
            i = i.next

    def display(self):
        i = self.head
        while i is not self.head:
            self.my_list.append(i.value)
            i = i.next


if __name__ == '__main__':
    doubly = DublyLinkedList()
    # Insert Values to the LinkedList at the beginning.
    doubly.insert_start(10)
    doubly.insert_start(20)
    doubly.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of Circular LinkedList')
    print(list(doubly))

