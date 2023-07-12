# DOUBLY LINKED LIST IMPLEMENTATION (for reference)

class Node:
    def __init__(self, data):
        self.data = data          # Data stored in the node
        self.prev = None          # Reference to the previous node
        self.next = None          # Reference to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None          # Reference to the first node
        self.tail = None          # Reference to the last node
        self.size = 0             # Number of nodes in the doubly linked list
    
    def is_empty(self):
        return self.size == 0     # Check if the doubly linked list is empty
    
    def __len__(self):
        return self.size          # Return the number of nodes in the doubly linked list
    
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1             # Increment the size of the doubly linked list
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1             # Increment the size of the doubly linked list
    
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Doubly linked list is empty.")
        
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1         # Decrement the size of the doubly linked list
                return
            current = current.next
        
        raise ValueError(f"{data} not found in the doubly linked list.")
