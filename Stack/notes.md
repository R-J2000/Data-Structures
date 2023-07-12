#### Stack

A stack is a linear data structure where insertion and removal of elements occur at the same end known as the top. It follows the Last-In-First-Out (LIFO) principle, meaning that the most recently added element is the first one to be removed. A common real-life example of a stack is a pile of plates, where the plate added last is placed on top, and the plate removed first is from the top. The removal operation is referred to as "popping" from the stack, while adding an element is called "pushing" onto the stack. The stack data structure provides a convenient and efficient way to manage elements, ensuring that the most recently added item is easily accessible and processed before the others. [See Attach Images]

Use Cases:

    a. Used in Depth First Search Implementation
    b. Used by undo mechanism in text editor
    c. Used in complier syntax to check for matching brackets 

Operation Costs:

    a. Popping --> O(1)
    b. Pushing --> O(1)
    c. Peeking --> O(1)
    d. Searching --> O(n)
    e. Size --> O(1)
    
**Popping & Pushing Operations for Stacks**

Push Operation:

    The push operation is used to add an element to the top of a stack. It involves two main steps:
    
        a. Incrementing the stack pointer or top index to indicate the new top position.
        b. Storing the new element at the updated top position in the stack's underlying data structure.
        
        In technical terms, the push operation involves updating the stack's internal state by increasing the stack pointer, 
        and then storing the new element at the memory location pointed to by the updated stack pointer.

Pop Operation:

    The pop operation is used to remove and retrieve the element from the top of a stack. It also involves two main steps:

        a. Retrieving the element from the top position in the stack's underlying data structure.
        b. Decrementing the stack pointer or top index to indicate the new top position after removal.
        
        In technical terms, the pop operation involves accessing the element stored at the current top position, 
        retrieving its value from the memory location, and then updating the stack's internal state by decrementing 
        the stack pointer to reflect the new top position after removal.
