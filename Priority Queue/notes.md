#### Priority Queue [See Attached Images]

A priority queue is an abstract data type that resembles a normal queue, but with each element assigned a specific priority. The priority assigned to an element determines the order in which it is removed from the priority queue. Elements with higher priority are dequeued before elements with lower priority. 

**Heap** -  A tree based data structure that satisfies the heap invariant/property. If A is a parent node of B, then A much be ordered relative to B (either greater than or less than), and this same order must hold for all Parent-Child nodes. [See Attached Images]

Note: The Data must be comparable in order to establish a priority

Use Cases:

    a. Used in some Dijkstra's Shortest Path Algorithm Implementations
    b. Anytime you want to fetch the next "best" or next "worst" element
    c. Minimum Spanning Tree Algorithms
    d. Used in BFS algorithms such as A*

Operation Costs:

    a. Binary Heap Construction --> O(n)
    b. Polling --> O(log(n))
    c. Peeking --> O(1)
    d. Adding --> O(log(n))
    e. Naive Removal --> O(n) [O(log(n)) in the case of hash table]
    f. Naive Contains --> O(n) [O(1) in the case of hash table]
    
**Insertion & Removal for Priority Queue with Binary Heap**

Insertion:

    a. To insert a new element into the priority queue, it is initially placed at the next available position in 
        the underlying binary heap, typically at the bottom-rightmost position to maintain the tree's shape.
    b. The element is then "bubbled up" or "percolated up" through the heap by comparing its priority with its parent node.
    c. If the priority of the new element is higher (or lower depending on the priority ordering used), 
        it is swapped with its parent node. This process is repeated until the element reaches its correct 
        position or reaches the root of the heap.

Removal:

    a. The removal operation in a priority queue with a binary heap always removes the element with the highest (or lowest) priority.
    b. The element at the root of the binary heap represents the element with the highest priority.
    c. To remove this element, it is swapped with the last element in the heap, typically the bottom-rightmost element.
    d. After the swap, the element is removed from the heap, and the heap property is temporarily violated since the new 
        root element may not be in the correct position.
    e. To restore the heap property, the new root element is "bubbled down" or "percolated down" through the heap by comparing 
        its priority with its children.
    f. The element is swapped with its higher-priority child (or lower-priority child depending on the priority ordering used) 
        until it reaches its correct position or becomes a leaf node.
