class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
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
        else:
            self.head = new_node
        self.length += 1

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.length += 1
        self.length += 1

    def insert(self, data, index):
        if index >= self.length:
            raise IndexError("Index out of bound")
            return
        if index == 0:
            self.insert_at_head(data)
        elif index == self.length - 1:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            curr_index = 0
            curr_node = self.head
            while curr_index < index - 1:
                curr_node = curr_node.next
                curr_index += 1
            next_node = curr_node.next
            curr_node.next = new_node
            new_node.next = next_node
            self.length += 1

    def find(self, data):
        if self.head:
            curr_node = self.head
            curr_index = 0
            while curr_node:
                if curr_node.data == data:
                    return (True, curr_index)
                curr_node = curr_node.next
                curr_index += 1
            return False, None
        else:
            return False, None

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

    def delete(self, data):
        if self.head:
            curr_node = self.head
            prev_node = None
            while curr_node:
                if curr_node.data == data:
                    if prev_node:
                        prev_node.next = curr_node.next
                    else:
                        self.head = None
                    self.length -= 1
                prev_node = curr_node
                curr_node = curr_node.next
        else:
            raise ValueError("Linked List is empty")


def test_():
    ll = LinkedList()
    ll.insert_at_end(10)
    assert ll.length == 1
    ll.insert_at_head(20)
    assert ll.length == 2
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert(50, 2)
    is_found, index = ll.find(40)
    ll.pretty_print()
    assert is_found
    assert index == 4
    prev_len = ll.length
    ll.delete(50)
    assert ll.length == prev_len - 1
