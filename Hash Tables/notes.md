#### Hash table

A hashtable, also known as a hash map, is a data structure that allows for efficient storage and retrieval of key-value pairs. It provides constant-time average-case complexity for insertions, deletions, and lookups, making it an important and widely used data structure in computer science. The Key must be unique, but values can be repeated.

**Hash Function**

The key concept behind hashtables is the use of a hash function. A hash function takes a key as input and produces an index or hash code, which represents the location in the array where the key-value pair will be stored. The hash function should ideally distribute the keys uniformly across the array, minimizing the chances of collisions (two different keys producing the same hash code).

When storing a key-value pair in a hashtable, the hash function is applied to the key to determine the appropriate index in the array. A hash function must be deterministic; if H(x) = y, then it must always equal y.  If multiple keys produce the same hash code (a collision), the hashtable uses a technique called collision resolution to handle it.

If x and y have the same hash function value (i.e H(x) == H(y)), they might be equal. But if the H(x) != H(y), then we know x != y. This is a quick and dirty way to check in constant time if two values are the same--where sich comparisons are more expensive.

Hashable - A key is hashable if its value never changes during its lifetime. This is ensured by making keys immutable.

Operation Cost

    a. Search --> O(1) [Assumes uniform hashing; Worst Case time is O(n))
    b. Insertion --> O(1) [Assumes uniform hashing; Worst Case time is O(n))
    c. Removal --> O(1) [Assumes uniform hashing; Worst Case time is O(n))

**Hash Collisions**

Separate Chaining

    Separate chaining is a collision resolution technique to store elements in a hash table, which is represented as an array of linked lists. 
    Each index in the table is a chain of elements mapping to the same hash value. When inserting keys into a hash table, we generate an index
    and mitigate collisions by adding a new element to the list at that particular index. Nonetheless, preventing duplicate keys in our table
    will slightly change the insert algorithm since we must ensure the key is not in the list.

Open Addressing

    Open addressing or closed hashing is the second most used method to resolve collision. This method aims to keep all the elements 
    in the same table and tries to find empty slots for values. Open addressing is named because the locations for the values 
    are not fixed and can be addressed to an empty slot if a collision happens. 

    This method resolves collisions by probing or searching through the hash table for indexes that are available for storing elements. 
    Unlike chaining, open addressing stores one value in each index.There are different approaches for these functions but the well-knowns are:
        a. Linear Probing
        b. Quadratic Probing
        c. Double Hashing
    
*Load Factor* - (Items in Table) / (Size of Table) (An important variable when considering open addressing) [See Attached Illustration]

Linear Probing

    In linear probing, the hash table is searched sequentially that starts from the original location of the hash. 
    If in case the location that we get is already occupied, then we check for the next location by using a linear functions.
    
    The biggest concern in the open addressing scheme is that of ending up in an infinite loop. This is resolved by ensuring that the gap between 
    two probes is 1. To do so, if we our probing funtion is P(x) = ax + b and N is the size of the hash table, we set a such that the Greatest 
    Common Denominator of a and N is 1.
    
    Removal - Removal can be tricky when using linear (or quadratic probing). The general procedure is to remove the key based on the same 
    probing formula as the insertions, however, for each removal add a unique marker or a "tombstone" to note the a value was removed. So that 
    in future removal operations we do not stop at a null node and declare that the key desired to be removed is not present in the table.
    
    Tombstones are generally granted the status of filled slots; however, in the case of a probe ending up at a tombstone spot, the tombstone is
    discard for the key-value pair.
    
Quadratic Probing
    
    Quadratic probing is much the same as linear probing, but instead of using a linear function to probe, a quadratic function is used.
    The advatage of this appraoch is that clustering observed in Linear probing can be avoided, however, the problems of ending up in a inifinte 
    loop presists. There are several ways to reslove this, below are two:
    
    a. Let P(x) = x^2, keep the table size a prime number greater than 3 and the load factor less than 1/2
    b. Let P(x) = (x^2 + x)/2, keep the table size a power of two
    
Double Hashing

    Double hashing is a collision resolution technique used in hash tables. It works by using two hash functions to compute two different 
    hash values for a given key. The first hash function is used to compute the initial hash value, and the second hash function is used 
    to compute the step size for the probing sequence. 
    
    The probing funciton probes according to a constant multiple of another hash function, specifically P(k, x) = x*H^2(k), where H^2(k) is 
    a second hash function.

    Double hashing has the ability to have a low collision rate, as it uses two hash functions to compute the hash value and the step size. 
    This means that the probability of a collision occurring is lower than in other collision resolution techniques such as linear 
    probing or quadratic probing. 

    However, double hashing has a few drawbacks. First, it requires the use of two hash functions, which can increase the computational 
    complexity of the insertion and search operations. Second, it requires a good choice of hash functions to achieve good performance. 
    If the hash functions are not well-designed, the collision rate may still be high.
    
    Constructing Secondary Hash Function - 
        

