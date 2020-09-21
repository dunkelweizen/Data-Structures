"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def set_next_node(self, next_node):
        self.next = next_node

    def set_prev_node(self, prev_node):
        self.prev = prev_node
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.set_next_node(self.head)
            self.head.set_prev_node(new_node)
            self.head = new_node

        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        ret_value = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.set_prev_node = None
        else:
            self.tail = None
        self.length -= 1
        return ret_value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
        else:
            new_node.set_prev_node(self.tail)
            self.tail.set_next_node(new_node)
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        ret_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.set_next_node(None)
        self.length -= 1
        return ret_value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if node.prev is None:
        #     print("Already head")
        #     break
        if node.next is not None:
            node.next.set_prev_node(node.prev)
        node.prev.set_next_node(node.next)
        self.head.set_prev_node(node)
        node.set_next_node(self.head)
        node.set_prev_node(None)
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.prev is not None:
            node.next.set_prev_node(node.prev)
            node.prev.set_next_node(node.next)
        elif node.next is None:
            self.tail = node
        else:
            node.next.set_prev_node(None)
            self.head = node.next
        self.tail.set_next_node(node)
        node.set_prev_node(self.tail)
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
        elif node.prev is None:
            node.next.set_prev_node(None)
            self.head = node.next
        elif node.next is None:
            node.prev.set_next_node(None)
            self.head = node.prev
        else:
            node.next.set_prev_node(node.prev)
            node.prev.set_next_node(node.next)
        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = 0
        if self.length == 1:
            max_value = self.head.value
        current_node = self.head
        while current_node.next is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        if current_node.value > max_value:
            max_value = current_node.value
        return max_value