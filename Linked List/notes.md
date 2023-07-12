#### Linked Lists

A linked list is a linear data structure consisting of nodes, where each node contains data and a reference to the next node in the sequence (in singly-linked-lists) and both forwards and backwards (in doubly-linked-lists). Linked lists excel at efficiently adding or removing elements at the beginning or end of the list, making them a flexible choice compared to arrays.

Terminology

    a. Head: First Node in Linked List
    b. Tail: last Node in Linked List
    c. Pointer: Reference to another node
    d. Node: An object containing data and pointer(s)

Use Cases

    a. List, Queue, Stack Implementations
    b. Cicular List Implementations
    c. Adjacency Lists for Graphs

**Singly Linked List**: 

    Advantages: Uses Less Memory; Simpler Implementation
    Disadvantages: Cannot easily access previous element

Operation Costs:
    
    a. Search --> O(n)
    b. Insertion at Head --> O(1)
    c. Insertion at Tail --> O(1)
    d. Remove at Head --> O(1)
    e. Remove at Tail --> O(n)
    f. Remove in Middle --> O(n)
    
**Doubly Linked List**:  

    Advantages: Can be traversed backwards
    Disadvantages: Takes 2x memory
    
Operation Costs:
    
    a. Search --> O(n)
    b. Insertion at Head --> O(1)
    c. Insertion at Tail --> O(1)
    d. Remove at Head --> O(1)
    e. Remove at Tail --> O(1) [Noteably different]
    f. Remove in Middle --> O(n)
