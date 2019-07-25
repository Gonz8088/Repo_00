# From: Python Data Structures and Alogrithms
# Benjamin Baka, Packt published 2017.

# Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):              # <---This needs work
        return str(self.data)

# Single Linked List
class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def __str__(self):
        return str(self.head)

    def append_node(self, data):
        node = Node(data)           # Encapsulate the data in a Node
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def delete_node(self, data):    # Delets a Node by using data as a reference
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def clear(self):
        """Clear the entire list. """
        self.tail = None
        self.head = None

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

# Double Linked List
