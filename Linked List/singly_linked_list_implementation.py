# SINGLY LINKED LIST IMPLEMENTATION (for reference)
class Node:
    def __init__(self, data):
        self.data = data          # Data stored in the node
        self.next = None          # Reference to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None          # Reference to the first node
        self.tail = None          # Reference to the last node
        self.size = 0             # Number of nodes in the singly linked list
    
    def is_empty(self):
        return self.size == 0     # Check if the singly linked list is empty
    
    def __len__(self):
        return self.size          # Return the number of nodes in the singly linked list
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1             # Increment the size of the singly linked list
    
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1             # Increment the size of the singly linked list
    
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Singly linked list is empty.")
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1         # Decrement the size of the singly linked list
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1     # Decrement the size of the singly linked list
                return
            current = current.next
        
        raise ValueError(f"{data} not found in the singly linked list.")
