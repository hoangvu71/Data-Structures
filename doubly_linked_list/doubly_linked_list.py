"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        # Wrap value in node
        new_node = ListNode(value)

        # Add length
        self.length += 1

        # if there's nothing in head or tail
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        
        # else add to head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        
        # Node to be deleted
        removed = self.head

        # Decrease length
        self.length -= 1

        # if there's nothing in head or tail
        if self.head == None and self.tail == None:
            return None
        
        # if there's one value on head and tail
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return removed.value
        
        # else remove head
        else:
            self.head = self.head.next
            self.head.prev = None
            return removed.value

        
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):

        # Wrap the value in a node
        new_node = ListNode(value)

        # Increases the length
        self.length += 1

        # if there's no head or tail
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node

        # else add to tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):

        # Wrap the node that will get removed
        removed = self.tail.value

        # Add length
        self.length -= 1

        # if there's no head or tail
        if self.head == None and self.tail == None:
            return None

        # if there's one value in head and tail
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return removed
        # else remove from tail
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return removed

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        
        # Wrap value in node
        move_node = node

        # does list contains this node?
        def contains_node(node):
            current_node = self.head
            while current_node != node and current_node.next != None:
                current_node = current_node.next
            if current_node == node:
                return [True, current_node]
            else:
                return False
        # if there's nothing in head and tail
        if self.head == None and self.tail == None:
            return None

        elif self.head == self.tail:
            self.head = move_node
            self.tail = move_node

        if contains_node(node)[0]:
            if self.length == 2:
                if self.tail == move_node:
                    self.tail.next = self.head
                    self.head = self.tail
                    self.tail = self.head.prev
                    self.head.prev = None
                    self.tail.next = None
                else:
                    return None
                
            if self.length > 2:
                # delete 
                current_node = contains_node(node)[1]
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

                # move to front
                self.head.prev = current_node
                current_node.next = self.head
                self.head = current_node
                self.head.prev = None
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
         # Wrap value in node
        move_node = node

        # does list contains this node?
        def contains_node(node):
            current_node = self.head
            while current_node != node and current_node.next != None:
                current_node = current_node.next
            if current_node == node:
                return [True, current_node]
            else:
                return False
        # if there's nothing in head and tail
        if self.head == None and self.tail == None:
            return None

        elif self.head == self.tail:
            self.head = move_node
            self.tail = move_node

        if contains_node(node)[0]:
            if self.length == 2:
                if self.head == move_node:
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    self.head = self.tail
                    self.tail = self.head.next
                    self.head.prev = None
                    self.tail.next = None
            
            if self.length > 2:
                 # delete 
                current_node = contains_node(node)[1]
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

                # move to tail
                self.tail.next = current_node
                current_node.prev = self.tail
                self.tail = current_node
                self.tail.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        delete_node = node

        # if there's nothing in head or tail
        if self.head == None and self.tail == None:
            return None

        # if there's one value in head and tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        # if there's more than two nodes
        if self.length >= 2:
            self.length -= 1
        
            # if the node was head:
            if self.head == delete_node:
                self.head.next.prev = None
                self.head = self.head.next

            # if the node was tail:
            elif self.tail == delete_node:
                self.tail = self.tail.prev
                self.tail.next = None

    """Returns the highest value currently in the list"""
    def get_max(self):
        
        # If there's nothing in list
        if self.head == None and self.tail == None:
            return None

        # if there's just one value
        if self.head == self.tail:
            return self.head.value

        # if there's more value
        if self.length > 1:
            current_node = self.head
            value_count = 0
            while current_node != None:
                if current_node.value > value_count:
                    value_count = current_node.value
                current_node = current_node.next
            return value_count
