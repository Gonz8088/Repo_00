# From: Python Data Structures and Alogrithms
# Benjamin Baka, Packt published 2017.

# Single Linked List
class NodeSLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):              # <---This needs work
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return str(self.head)

    def append_node(self, data):
        node = NodeSLL(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def delete_node(self, data):
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
class NodeDLL(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)       # <---This needs work

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_node(self, data):
        """ Append an item to the list. """
        new_node = NodeDLL(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def delete_node(self, data):
        """ delete_node uses the data passed to it to look up which node to delete """
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -=1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

# Circular Linked list
class NodeCLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):              # <---This needs work
        return str(self.data)

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return str(self.head)

    def append_node(self, data):
        node = NodeSLL(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def delete_node(self, data):
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

# Stack
class NodeStack:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = NodeStack(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
