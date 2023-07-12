# QUEUE IMPLEMENTATION WITH LINKED LIST (for reference)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None   # Reference to the front of the queue
        self.rear = None    # Reference to the rear of the queue
        self.size = 0       # Number of elements in the queue

    def is_empty(self):
        return self.size == 0  # Check if the queue is empty

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1          # Increment the size of the queue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1          # Decrement the size of the queue
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek an empty queue.")
        return self.front.data

    def size(self):
        return self.size       # Return the current size of the queue
