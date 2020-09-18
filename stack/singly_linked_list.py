class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            if self.head.get_next_node() is None:
                head = self.head
                self.head = None
                self.tail = None
                return head.get_value()
            value = self.head.get_value()
            self.head = self.head.get_next_node()
            return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next_node() is not self.tail:
            current = current.get_next_node()
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next_node()
        return False

    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        max_value = 0
        while cur_node is not None:
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()
        return max_value

    # def __iter__(self):
    #     return LinkedListIterator(self)

    def __len__(self):
        copy = self
        if copy.head is None and copy.tail is None:
            return 0
        elif copy.head == copy.tail:
            return 1
        else:
            count = 1
            while copy.head.get_next_node():
                copy.remove_head()
                count += 1
            return count


# class LinkedListIterator:
#     def __init__(self, linkedlist):
#         self._linkedlist = linkedlist
#         self._index = 0
#         self.current_node = self._linkedlist.head
#
#     def __next__(self):
#         if self._linkedlist.head is None and self._linkedlist.tail is None:
#             return None
#         elif self._linkedlist.head == self._linkedlist.tail:
#             return None
#         if self._index < len(self._linkedlist):
#             next_node = self.current_node.get_next_node()
#             self._index += 1
#             self.current_node = self.current_node.next_node
#             return next_node
#         raise StopIteration