class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CirclularLinkedList:
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
    circular = CirclularLinkedList()
    # Insert Values to the CirclularLinkedList at the beginning.
    circular.insert_start(10)
    circular.insert_start(20)
    circular.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of Circular LinkedList')
    print(list(circular))

