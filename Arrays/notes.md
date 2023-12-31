#### Arrays
Arrays are ordered collections of data that store values at contiguous memory locations and can be accessed using an index. They provide efficient read access but tend to have limitations when it comes to insertions or deletions due to the required shifting of elements.

**Static and Dynamic Arrays**: 
1. Static Array - a fixed length container with n element, indexable from [0, n-1]. Static arrays are given contigous chunks of memory. 
2. Dynamic Array - a container that can grow and shrink in size

Use cases:

    a. Storing and accessing sequential data
    b. Temporarily storing objects
    c. Lookup Table (due to indexable)
    d. Cache answers to subproblems

**Operation Costs**

Static Array:    

    a. Access --> O(1)      
    b. Search --> O(n)     
    c. Insertion/Appending/Deletion --> n/a 
    
Dynamic Array:

    a. Access --> O(1)
    b. Search --> O(n)
    c. Insertion --> O(n)
    d. Appending --> O(1)
    e. Deletion --> O(n) 

**Heterogeneous and Homogeneous Data Types** - Arrays in different languages have different functionalities; in Java and Swift one can only store one type of value in an array; in Python many different kinds of values can be stored. Both these approaches have advantages and disadvantages. A key advantage of homogeneous arrays is that all values can be stored in a contiguous block of memory. For heterogeneous arrays this is not possible. Python, therefore, stores references to the distinct types of objects in the array and stores the actual object at different spots. 
