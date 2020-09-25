"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if current node value is less than new value, go right
        if self.value < value:
            # if right child does not exist, add it
            if not self.right:
                self.right = BSTNode(value)
            # if child does exist, repeat process
            else:
                self.right.insert(value)
        # if current node is greater than new value, go left
        elif self.value > value:
            # if left child does not exist, add it
            if not self.left:
                self.left = BSTNode(value)
            # if child does exist, repeat
            else:
                self.left.insert(value)
        # if node is empty, create it as node(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self is None:
            return False
        elif self == target:
            return True
        else:
            while self.value is not target:
                if self.value < target:
                    if self.right is None:
                        return False
                    else:
                        self = self.right
                else:
                    if self.left is None:
                        return False
                    else:
                        self = self.right
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # go right as long as right child exists
        current_node = self
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #need to travel all the way to the left
        #then backtrack, printing each node, then printing the right child
        #once back at root node, repeat process with right side
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()




    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
print("in order")
bst.in_order_print()
# print("post order")
# bst.post_order_dft()
