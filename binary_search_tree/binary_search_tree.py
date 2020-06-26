
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
        
        # Is tree empty?
        if self.value == None:
            self.value = value
        
        # if value less than root?
        if value < self.value:

            # if left leaf is still available
            if self.left == None:
                self.left = BSTNode(value)

            # if left leave is occuplied, call insert
            else:
                self.left.insert(value)

        # if value more or equal to root
        if value >= self.value:

            # if right leaf is still available
            if self.right == None:
                self.right = BSTNode(value)

            # else call insert on right leaf
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # is the root equal to target
        if self.value == target:
            return True

        # if left leaf not empty

        elif self.left != None and target < self.value:
                return self.left.contains(target)

        # if right leaf not empty
        elif self.right != None and target >= self.value:
                return self.right.contains(target)

        else:
            return None
    # Return the maximum value found in the tree
    def get_max(self):
        
                
        # if right leaf is not available
        # it means self.value is the biggest value
        if self.right == None:
            return self.value
        
        # if right leaf is available
        # call right leaf get_max()
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # is left available?
        fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        
        # is right available?
        if self.right != None:
            self.right.for_each(fn)



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

