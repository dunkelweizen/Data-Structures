"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
   class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        count = 0
        for _ in self.storage:
            count += 1
        return count

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            return self.storage.pop(-1)
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.storage.head = None

    def __len__(self):
        return self.size

    def push(self, value):
        if self.storage.head is None:
            self.storage.head = Node(value)
        else:
            new_node = Node(value)
            new_node.set_next_node(self.storage.head)
            self.storage.head = new_node
        self.size += 1

    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
