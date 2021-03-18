class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.my_list = []

    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        i = self.head

        while i.next != self.tail:
            i = i.next
        new_node = Node(value)
        i.next = new_node
        new_node.next = self.tail

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
        self.display()
        return str(self.my_list)


if __name__ == '__main__':
    single_list = SingleLinkedList()
    # Insert Values to the LinkedList at the beginning.
    single_list.insert_start(10)
    single_list.insert_start(20)
    single_list.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of LinkedList')
    print(list(single_list))
    single_list.insert_end(100)
    single_list.insert_end(200)
    single_list.insert_end(300)
    print('Linkedlist after inserting 100,200,300 at the end of LinkedList')
    print(list(single_list))
    print(f'Display LinkedList as list :: __str__ implementation is called')
    print(single_list)
