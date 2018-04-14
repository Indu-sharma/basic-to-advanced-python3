class Node(object):
    def __init__(self, info):
        self.info = info
        self.link = None

    def set_data(self, data):
        self.info = data

    def set_link(self, node):
        self.link = node

    def get_data(self):
        return self.info

    def get_link(self):
        return self.link


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_link(self.head)
        self.head = new_node

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_link()
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.get_data()
            current = current.get_link()

    def __eq__(self, other):
        if len(self) == len(other) and all(a == b for a, b in zip(self, other)):
            return True
        else:
            return False

    def __str__(self):
        return str([i for i in self])

    def __repr__(self):
        return repr("{}({})".format(self.__class__.__name__, str(self)))

    def __mul__(self, other):
        return [a * b for a, b in zip(self, other)]

    def __add__(self, other):
        return [a + b for a, b in zip(self, other)]

    def __sub__(self, other):
        return [a - b for a, b in zip(self, other)]
    
    def test_len(createlinklists):
        a, b = createlinklists
        assert len(a) == 5
