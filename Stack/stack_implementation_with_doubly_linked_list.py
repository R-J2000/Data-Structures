# STACK IMPLEMENTATION WITH DOUBLY LINKED LIST (for reference)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Reference to the topmost node in the stack
        self.size = 0   # Number of elements in the stack

    def is_empty(self):
        return self.size == 0  # Check if the stack is empty

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node
        self.size += 1  # Increment the size of the stack

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
        popped_item = self.top.data
        if self.top.prev:
            self.top.prev.next = None
            self.top = self.top.prev
        else:
            self.top = None
        self.size -= 1  # Decrement the size of the stack
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek an empty stack.")
        return self.top.data

    def size(self):
        return self.size  # Return the current size of the stack
