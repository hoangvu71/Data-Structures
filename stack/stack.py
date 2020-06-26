"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         count = 0
#         current_node = self.storage.head
#         while current_node != None:
#           count += 1
#           current_node = current_node.next_node
#         else:
#           return count

#     def push(self, value):
#         self.storage.add_to_head(value)

#     def pop(self):
#         if self.storage.head == None:
#             return None
#         else:
#             return self.storage.remove_head()

class Stack:
    def __init__(self):
      self.size = 0
      self.storage = []

    def __len__(self):
      return self.size


    def push(self, value):
      self.size += 1
      return self.storage.insert(0, value)



    def pop(self):
      if self.size == 0:
        return None
      self.size -= 1
      popped_ele = self.storage[0]
      self.storage.remove(popped_ele)
      return popped_ele