class Queue:

    def __init__(self):
        self.list = []

    def isEmpty(self):

        if not self.list:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue Underflow')
        else:
            return self.list.pop(0)

    def __str__(self):
        return '\n'.join(map(str, self.list))


if __name__ == '__main__':
    Obj = Queue()
    Obj.enqueue(110)
    Obj.enqueue(20)
    Obj.enqueue(30)
    Obj.enqueue(200)
    Obj.enqueue(9)
    print(f'Initial Queue is :\n{Obj}')
    Obj.dequeue()
    Obj.dequeue()
    Obj.dequeue()
    print(f'Deque after 3 pop is :\n{Obj}')
