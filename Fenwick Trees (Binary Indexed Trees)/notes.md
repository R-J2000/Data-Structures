#### Fenwick Trees (Binary Indexed Tree)

A Fenwick tree, also known as a binary indexed tree (BIT), is a data structure used to efficiently perform operations on a dynamic array or list of numbers. It allows for efficient computation of cumulative sum queries and updates in logarithmic time complexity.

The structure of a Fenwick tree is based on a binary representation of indices. Each index in the tree represents a range of elements in the original array, and each node in the tree contains the cumulative sum of elements within that range.

Fenwick trees support two main operations:

    a. Prefix Sum Query: Given an index i, you can compute the sum of elements from index 1 to i in logarithmic time complexity.
    b. Update: Given an index i and a value v, you can update the value of the element at index i in logarithmic time complexity. 
        The tree is modified to reflect the update and maintain the cumulative sum property.

The key insight of Fenwick trees lies in representing indices in binary form. By manipulating the binary representation, you can efficiently navigate the tree to perform the desired operations.

Operation Cost

    a. Construction --> O(n)
    b. Point Update --> O(log(n))
    c. Range Sum --> O(log(n))
    d. Range Update --> O(log(n))
    e. Add/Remove Index --> n/a

In a Fenwick tree, a cell can be responsible for other cells. The position of the least significant bit (LSB) determines the range of responsibilties a cell to the cells below itself. For example, if index = 12 = 1100 (in binary representation). The LSB is 100 or 3. Thus, the cell at index 12 will be responsible for 2^(3-1) = 4 cells below itself.

In the case of ranged sum queries, being "responsible" for 4 cells below yourself, is to have the sum of the 4 cells below oneself stored somewhere handy.

*Point Updates* - If a data value is being updated in under Fenwick regime, all the cells responsible for the cell being updated must also be modified. To update cell 9, cells 10, 12 and 16, all must be updated as they are all responsible of cell 9.

**Fenwick Tree Construction**

Linear Construction

    The linear construction of a Fenwick tree refers to the process of building the tree from an initial array of values in a linear time 
        complexity, specifically O(n), where n is the number of elements in the array.

    Here's a step-by-step explanation of the linear construction process for a Fenwick tree:

    Start with an input array of values, let's call it inputArray, where the elements are indexed from 1 to n. Initialize a Fenwick tree, 
        let's call it fenwickTree, with all elements set to 0.

    Iterate over each index i from 1 to n.

    At each index i, update the corresponding element in the Fenwick tree using the following steps:

        a. Start with the current index i.

        b. Find the next index j by adding the least significant bit (LSB) of i to i itself. The LSB can be obtained using the bitwise 
            AND operation with the two's complement of i: j = i + (i & -i).

        c. Repeat the process until j exceeds n. 

        This process effectively accumulates the values in the Fenwick tree, such that each index i stores the cumulative sum of a 
            specific range of elements in the inputArray.

    After completing the above steps for all indices, the Fenwick tree is fully constructed.

    The linear construction of a Fenwick tree is based on the binary representation of indices and the accumulation of values using the 
    LSB trick. By following this process, you can efficiently build the Fenwick tree with a time complexity of O(n), making it more efficient 
    than constructing other data structures like segment trees in O(n log n) time complexity.
