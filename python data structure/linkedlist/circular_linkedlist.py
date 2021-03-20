class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.my_list = []

    def createCll(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node

    def insert_start(self, value):
        if not self.head:
            self.createCll(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def delete_start(self):

        if not self.head:
            pass
        else:
            to_del = self.head
            i = self.head.next
            self.tail.next = i
            self.head = i
            print(f'First element of Circular LL - {to_del.value} is deleted.')

    def delete_end(self):

        if not self.head:
            pass
        else:
            i = self.head
            while i.next != self.tail:
                i = i.next
            to_del = i.next
            i.next = self.head
            self.tail = i
            print(f'Last element of Circular LL - {to_del.value} is deleted.')

    def insert_end(self, value):
        if not self.head:
            self.createCll(value)
        else:
            i = self.head
            while i.next != self.head:
                i = i.next
            new_node = Node(value)
            i.next = new_node
            new_node.next = self.head
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


if __name__ == '__main__':
    circular = CircularLinkedList()
    # Insert Values to the CircularLinkedList at the beginning.
    circular.createCll(100)
    circular.insert_start(10)
    circular.insert_start(20)
    circular.insert_start(30)
    circular.insert_end(1000)
    circular.insert_end(2000)
    circular.insert_end(3000)
    print('->'.join(map(str,circular)))
    circular.delete_start()
    print('->'.join(map(str,circular)))
    circular.delete_end()
    print('->'.join(map(str, circular)))
