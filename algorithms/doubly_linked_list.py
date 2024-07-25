class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node
        else:
            self.head = new_node
        self.length += 1

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
        self.length += 1

    def insert(self, data, index):
        if index < self.length:
            if index == 0:
                self.insert_at_head(data)
            else:
                new_node = Node(data)
                curr_node = self.head
                curr_index = 0
                while curr_node:
                    if index == curr_index:
                        curr_node.prev.next = new_node
                        new_node.prev = curr_node.prev
                        curr_node.prev = new_node
                        new_node.next = curr_node
                        self.length += 1
                        return
                    curr_node = curr_node.next
                    curr_index += 1
        else:
            raise IndexError("index out of bound")

    def find(self, data):
        if self.head:
            curr_node = self.head
            index = 0
            while curr_node:
                if data == curr_node.data:
                    return True, index
                curr_node = curr_node.next
                index += 1
        return False, None

    def delete(self, data):
        if self.head:
            curr_node = self.head
            while curr_node:
                if curr_node.data == data:
                    curr_node.prev = curr_node.next
                    self.length -= 1
                curr_node = curr_node.next
        else:
            raise ValueError("Doubly Linked List is empty")

    def pretty_print(self):
        elements = []
        if self.head:
            curr_node = self.head
            while curr_node:
                elements.append(curr_node.data)
                curr_node = curr_node.next
            print(elements)
        else:
            print("Linked List is empty")


def test_():
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    assert dll.length == 1
    dll.insert_at_head(20)
    assert dll.length == 2
    dll.insert(30, 1)
    assert dll.length == 3
    is_found, index = dll.find(30)
    assert is_found
    assert index == 1
    dll.delete(30)
    assert dll.length == 2
