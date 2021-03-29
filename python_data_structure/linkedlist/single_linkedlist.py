class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createSl(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def insert_start(self, value):
        if not self.head:
            self.createSl(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, value):
        if not self.head:
            self.createSl(value)
        else:
            i = self.head
            while i.next is not None:
                i = i.next
            new_node = Node(value)
            i.next = new_node
            new_node.next = None

    def __iter__(self):
        """
        This makes LinkedList an Iterable.
        """
        i = self.head
        while i is not None:
            yield i.value
            i = i.next

    def __str__(self):
        return '->'.join([str(i) for i in self])


if __name__ == '__main__':
    single_list = SingleLinkedList()
    # Insert Values to the LinkedList at the beginning.
    single_list.insert_start(10)
    single_list.insert_start(20)
    single_list.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of LinkedList')
    print(single_list)
    single_list.insert_end(100)
    single_list.insert_end(200)
    single_list.insert_end(300)
    print('Linkedlist after inserting 100,200,300 at the end of LinkedList')
    print(single_list)
