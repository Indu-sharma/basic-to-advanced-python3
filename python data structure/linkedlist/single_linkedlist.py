class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def display(self):
        i = self.head

        while i != None:
            print(i.value)
            i = i.next


if __name__ == '__main__':
    single_list = SingleLinkedList()
    # Insert Values to the LinkedList at the beginning.
    single_list.insert_start(10)
    single_list.insert_start(20)
    single_list.insert_start(30)
    print('Linkedlist after inserting 10,20,30 at the beginning of LinkedList')
    single_list.display()
    single_list.insert_end(100)
    single_list.insert_end(200)
    single_list.insert_end(300)
    print('Linkedlist after inserting 100,200,300 at the end of LinkedList')
    single_list.display()
