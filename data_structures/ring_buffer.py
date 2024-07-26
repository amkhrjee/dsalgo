# ring buffer = circular buffer = circular queue
class RingBuffer:
    def __init__(self, capacity):
        self.rb = [None] * capacity
        self.capacity = capacity
        self.head, self.tail = 0, 0
        self.size = 0

    def is_empty(self):
        return len(self.rb) == 0

    def enqueue(self, item):
        self.rb[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        if self.size > self.capacity:
            self.size = self.capacity
            self.head = (self.head + 1) % self.capacity

    def deque(self):
        if not self.is_empty():
            item = self.rb[self.head]
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return item

    def peek(self):
        if not self.is_empty():
            return self.rb[self.head]

    def is_full(self):
        return self.size == self.capacity


def test_():
    rb = RingBuffer(4)
    rb.enqueue(10)
    assert rb.size == 1
    rb.enqueue(20)
    rb.enqueue(30)
    rb.enqueue(40)
    rb.enqueue(50)
    assert rb.peek() == 20
    rb.deque()
    assert rb.peek() == 30
