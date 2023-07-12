# QUEUE IMPLEMENTATION WITH ARRAY (for reference)

class Queue:
    def __init__(self):
        self.queue = []    # Internal list to store queue elements

    def is_empty(self):
        return len(self.queue) == 0   # Check if the queue is empty

    def enqueue(self, item):
        self.queue.append(item)       # Add item to the end of the queue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")
        return self.queue.pop(0)     # Remove and return the first item from the queue

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek an empty queue.")
        return self.queue[0]         # Return the first item without removing it

    def size(self):
        return len(self.queue)       # Return the current size of the queue
