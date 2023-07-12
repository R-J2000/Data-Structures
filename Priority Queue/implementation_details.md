**Implentation Details**

The PriorityQueue class represents a priority queue using a binary heap. 
The heap is implemented as a list (self.heap), and various methods are defined to perform operations on the heap.
The is_empty method checks if the priority queue is empty. The parent, left_child, and right_child methods calculate 
the indices of the parent and child nodes in the binary heap. The swap method swaps elements at two given indices.

The heapify_up method restores the heap property by moving an element up in the heap. The heapify_down method restores 
the heap property by moving an element down in the heap. These methods are used to maintain the heap property after enqueue and dequeue operations.

The enqueue method adds an item to the priority queue by appending it to the end of the heap and then restoring the heap property. 
The dequeue method removes and returns the item with the highest priority by swapping it with the last element, removing the last 
element from the heap, and then restoring the heap property. The peek method returns the item with the highest priority without removing it.
This implementation ensures that items are inserted and removed from the priority queue based on their priority, maintaining the order 
defined by the binary heap structure.
