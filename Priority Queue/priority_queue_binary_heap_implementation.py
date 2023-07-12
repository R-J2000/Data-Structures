# PRIOITY QUEUE WITH BINARY HEAP (for reference)

class PriorityQueue:
    def __init__(self):
        self.heap = []   # Internal list to store the elements of the priority queue

    def is_empty(self):
        return len(self.heap) == 0   # Check if the priority queue is empty

    def parent(self, index):
        return (index - 1) // 2   # Calculate the parent index of a given index

    def left_child(self, index):
        return 2 * index + 1   # Calculate the left child index of a given index

    def right_child(self, index):
        return 2 * index + 2   # Calculate the right child index of a given index

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]   # Swap elements at given indices

    def heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)   # Move up in the heap to restore the heap property

    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left   # Determine the index of the smallest child

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right   # Determine the index of the smallest child

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)   # Move down in the heap to restore the heap property

    def enqueue(self, item):
        self.heap.append(item)   # Add the item to the end of the heap
        self.heapify_up(len(self.heap) - 1)   # Restore the heap property by moving the item up

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty. Cannot dequeue from an empty queue.")
        self.swap(0, len(self.heap) - 1)
        dequeued_item = self.heap.pop()   # Remove and return the item with the highest priority
        self.heapify_down(0)   # Restore the heap property by moving the new root down
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty. Cannot peek an empty queue.")
        return self.heap[0]   # Return the item with the highest priority without removing it
