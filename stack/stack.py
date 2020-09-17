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
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        copy = self
        try:
            copy.storage.head.get_value()
            count = 1
        except AttributeError:
            return 0
        while copy.storage.head.get_next_node():
            copy.storage.remove_head()
            count += 1
        return count

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            return self.storage.remove_tail()

