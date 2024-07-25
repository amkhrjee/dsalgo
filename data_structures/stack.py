class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def size(self):
        return len(self.stack)

    def pretty_print(self):
        print(self.stack)


def test_():
    s = Stack()
    s.push(10)
    assert s.size() == 1
    s.pop()
    assert s.size() == 0
