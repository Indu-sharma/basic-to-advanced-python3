class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.my_list = []

    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node

    def insert_end(self, value):
        i = self.head

        while i.next != self.tail:
            i = i.next
        new_node = Node(value)
        i.next = new_node
        new_node.next = self.tail
        new_node.prev = i

    def __iter__(self):
        """
        This makes LinkedList an Iterable.
        """
        i = self.head
        while i is not None:
            yield i.value
            i = i.next

    def display(self):
        i = self.head
        while i is not None:
            self.my_list.append(i.value)
            i = i.next

    def __str__(self):
        return ','.join([str(i) for i in self])


if __name__ == '__main__':
    doubly = DublyLinkedList()
    # Insert Values to the LinkedList at the beginning.
    doubly.insert_start(10)
    doubly.insert_start(20)
    doubly.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of LinkedList')
    print(list(doubly))
    doubly.insert_end(100)
    doubly.insert_end(200)
    doubly.insert_end(300)
    print('Linkedlist after inserting 100,200,300 at the end of LinkedList')
    print(list(doubly))
    print(f'Display LinkedList as list :: __str__ implementation is called')
    print(doubly)
