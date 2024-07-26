class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, data):
        self.q.append(data)

    def deque(self):
        self.q.pop(0)

    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)


def test_():
    q = Queue()
    q.enqueue(10)
    assert q.size() == 1
    q.enqueue(20)
    q.deque()
    assert q.size() == 1
    assert q.peek() == 20
