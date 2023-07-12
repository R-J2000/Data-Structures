# STACK IMPLEMENTATION WITH ARRAY (for reference)

class Stack:
    def __init__(self):
        self.stack = []       # Internal list to store stack elements

    def is_empty(self):
        return len(self.stack) == 0   # Check if the stack is empty

    def push(self, item):
        self.stack.append(item)       # Add item to the top of the stack

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
        return self.stack.pop()      # Remove and return the topmost item from the stack

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek an empty stack.")
        return self.stack[-1]        # Return the topmost item without removing it

    def size(self):
        return len(self.stack)       # Return the current size of the stack
