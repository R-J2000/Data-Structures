#### Queue

A queue is a linear data structure that is open at both ends and the operations are performed in First-in-First-out (FIFO) order. We define a queue to be a list in which all additions to the list are made at one end, and all deletions from the list are made at the other end.  The element which is first pushed into the order, the delete operation is first performed on that. To remove an element you “dequeue” it from the Queue. To add an element to the stack, you “enqueue” it. 

Use Cases:

    a. Used in Breadth First Search Implementation
    b. Keep track of x most recently added elements
    c. Any service operating on a first come first serve basis 

Operation Costs:

    a. Enqueue --> O(1)
    b. Dequeue --> O(1)
    c. Peeking --> O(1)
    d. Contains --> O(n)
    e. Removal --> O(n)
    f. Is Empty --> O(1)
    
**Enqueue & Dequeue Operations in Queues**

Enqueue Operation:
        
    The enqueue operation is used to add an element to the rear or end of a queue. It involves two main steps:

        a. Inserting the new element at the rear position in the queue's underlying data structure.
        b. Updating the rear pointer or tail index to indicate the new rear position.
        
        In technical terms, the enqueue operation involves modifying the queue's internal state by inserting 
        the new element at the appropriate memory location in the underlying data structure and then updating 
        the rear pointer or tail index to reflect the new rear position.

Dequeue Operation:

    The dequeue operation is used to remove and retrieve the element from the front or head of a queue. It also involves two main steps:

        a. Retrieving the element from the front position in the queue's underlying data structure.
        b. Updating the front pointer or head index to indicate the new front position after removal.
        
        In technical terms, the dequeue operation involves accessing the element stored at the current front position, 
        retrieving its value from the memory location, and then updating the queue's internal state by incrementing the 
        front pointer or head index to reflect the new front position after removal.
