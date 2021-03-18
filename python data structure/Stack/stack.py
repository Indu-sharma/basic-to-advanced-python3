"""
Stack Implementation Using List.
"""

class Stack:

    def __init__(self):
        self.list = []

    def isEmpty(self):

        if not self.list:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack Underflow')
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.list[-1]

    def __str__(self):
        return '\n'.join(map(str, reversed(self.list)))


if __name__ == '__main__':
    Obj = Stack()
    Obj.push(110)
    Obj.push(20)
    Obj.push(30)
    Obj.push(200)
    Obj.push(9)
    print(f'Initial Stack is :\n{Obj}')
    print(f'Top of the Stack is : {Obj.peek()}')
    Obj.pop()
    Obj.pop()
    Obj.pop()
    print(f'Stack after 3 pop is :\n{Obj}')
