#### Indexed Priority Queue

An index priority queue, also known as an indexed heap, is a data structure that maintains a collection of elements along with their priorities or keys. It allows efficient access to the element with the highest priority and supports operations such as insertion, deletion, and priority updates in logarithmic time complexity.

In an index priority queue, each element is associated with an index that uniquely identifies it. The index provides a way to track and access elements efficiently. The priority queue uses a heap-based data structure internally to maintain the elements in a partially ordered manner based on their priorities.

Advantages of using an index priority queue:

    a. Efficient Priority Access: The index priority queue allows quick access to the element with the highest priority. This is useful in 
        scenarios where processing elements based on their priorities is a key requirement.

    b. Fast Insertion and Deletion: Inserting and deleting elements in an index priority queue have a time complexity of O(log n), where n 
        is the number of elements in the queue. This makes it efficient for dynamic scenarios where elements are added or removed frequently.

    c. Priority Updates: The index priority queue supports updating the priority of an element. If the priority of an element changes, it 
        can be easily updated in the queue while maintaining the proper ordering. This is valuable when priorities dynamically change during 
        the execution of an algorithm or application.

    d. Element Indexing: The index associated with each element allows direct access and efficient operations specific to elements in the queue. 
        For example, finding and updating the priority of a specific element can be done in O(log n) time complexity instead of performing a 
        linear search.

Disadvantages of using an index priority queue:

    a. Additional Memory Overhead: The index priority queue requires additional memory to store the indices and maintain the internal heap 
        structure. This can be a consideration in memory-constrained environments or when dealing with very large datasets.

    b. Additional Complexity: Implementing and working with an index priority queue can be more complex than using a simple priority queue. 
        Managing the indices and ensuring proper synchronization between the indices and the underlying heap operations can add complexity 
        to the code.

    c. Limited to Unique Indices: Each index in the index priority queue must be unique. This constraint means that elements with duplicate 
        indices cannot coexist in the queue. If duplicate indices are required, additional handling or modifications to the data structure 
        may be necessary.

Index priority queues are commonly used in various algorithms and applications, such as Dijkstra's algorithm, Prim's algorithm, event-driven simulations, task scheduling, and more. The advantages of efficient priority access, fast insertion and deletion, priority updates, and element indexing make it a valuable tool for managing elements based on their priorities.

Operation Cost

    a. delete key index --> O(Log(n))
    b. value of key index --> O(1)
    c. contains key index --> O(1)
    d. peek min key index --> O(1)
    e. poll min key index --> O(Log(n))
    f. peek min index --> O(1)
    g. poll min index --> O(Log(n))
    h. insert key index + value --> O(Log(n))
    i. update key index + value --> O(Log(n))
    j. decreaseKey(key-index, value) --> O(Log(n)) 
    k. increaseKey(key-index, value) --> O(Log(n))
    
    The decreaseKey and increaseKey operations are a more constrained form of update.
