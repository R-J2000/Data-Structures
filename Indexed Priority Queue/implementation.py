# IMPLEMENTATION OF INDEXED PRIORITY QUEUE (for reference)

class IndexedPriorityQueue:
    def __init__(self):
        """
        Initialize the indexed priority queue.
        """
        self.queue = []
        self.index_map = {}

    def is_empty(self):
        """
        Check if the indexed priority queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def contains_index(self, index):
        """
        Check if the indexed priority queue contains the given index.

        Args:
            index: The index to check.

        Returns:
            bool: True if the index is present, False otherwise.
        """
        return index in self.index_map

    def size(self):
        """
        Get the size of the indexed priority queue.

        Returns:
            int: The size of the queue.
        """
        return len(self.queue)

    def insert(self, index, priority):
        """
        Insert an element with the given index and priority into the queue.

        Args:
            index: The index of the element.
            priority: The priority of the element.
        """
        if self.contains_index(index):
            raise ValueError("Index already exists in the queue.")
        
        self.queue.append((index, priority))
        self.index_map[index] = len(self.queue) - 1
        self._sift_up(len(self.queue) - 1)

    def update_priority(self, index, new_priority):
        """
        Update the priority of the element with the given index.

        Args:
            index: The index of the element.
            new_priority: The new priority of the element.
        """
        if not self.contains_index(index):
            raise ValueError("Index does not exist in the queue.")

        queue_index = self.index_map[index]
        old_priority = self.queue[queue_index][1]
        self.queue[queue_index] = (index, new_priority)
        
        if new_priority < old_priority:
            self._sift_up(queue_index)
        elif new_priority > old_priority:
            self._sift_down(queue_index)

    def delete(self, index):
        """
        Delete the element with the given index from the queue.

        Args:
            index: The index of the element to delete.
        """
        if not self.contains_index(index):
            raise ValueError("Index does not exist in the queue.")

        queue_index = self.index_map[index]
        last_index = len(self.queue) - 1

        self._swap(queue_index, last_index)
        del self.index_map[index]
        self.queue.pop()
        
        if queue_index != last_index:
            self._sift_up(queue_index)
            self._sift_down(queue_index)

    def get_min(self):
        """
        Get the element with the minimum priority from the queue.

        Returns:
            tuple: A tuple containing the index and priority of the minimum element.
        """
        if self.is_empty():
            raise ValueError("Queue is empty.")

        return self.queue[0]

    def _sift_up(self, queue_index):
        """
        Move the element at the given index up the heap if its priority is smaller.

        Args:
            queue_index: The index of the element in the queue.
        """
        while queue_index > 0 and self.queue[queue_index][1] < self.queue[(queue_index - 1) // 2][1]:
            parent_index = (queue_index - 1) // 2
            self._swap(queue_index, parent_index)
            queue_index = parent_index

    def _sift_down(self, queue_index):
        """
        Move the element at the given index down the heap if its priority is larger.

        Args:
            queue_index: The index of the element in the queue.
        """
        n = len(self.queue)
        while True:
            left_child_index = 2 * queue_index + 1
            right_child_index = 2 * queue_index + 2
            smallest_index = queue_index

            if left_child_index < n and self.queue[left_child_index][1] < self.queue[smallest_index][1]:
                smallest_index = left_child_index
            if right_child_index < n and self.queue[right_child_index][1] < self.queue[smallest_index][1]:
                smallest_index = right_child_index

            if smallest_index == queue_index:
                break

            self._swap(queue_index, smallest_index)
            queue_index = smallest_index

    def _swap(self, i, j):
        """
        Swap elements at the given indices.

        Args:
            i: The first index.
            j: The second index.
        """
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
        self.index_map[self.queue[i][0]] = i
        self.index_map[self.queue[j][0]] = j
