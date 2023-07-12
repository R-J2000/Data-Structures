#### Union Find [See Attached Pictures]

The Union-Find data structure, also known as the disjoint-set data structure, is a data structure used to efficiently manage a partitioning of elements into disjoint sets. It keeps track of a collection of disjoint sets, where each set contains a group of elements.

The key operations in the Union-Find data structure are:

    a. MakeSet(x): Creates a new set with a single element 'x' and assigns it a unique identifier.
    b, Find(x): Finds and returns the representative or root element of the set that 'x' belongs to. The root element represents the entire set.
    c. Union(x, y): Combines the sets that contain elements 'x' and 'y' into a single set by merging their respective sets. 
        The representative of one set becomes the representative of the merged set.

Use Cases:

    a. Kruskal's Minimum Spanning Tree Algorithim
    b. Network Connectivity
    c. Least Common Ancestor in Trees
    
Operation Cost:

    a. Construction --> O(n)
    b. Union --> 𝛼(𝑛) [ammortized constant time ~ almost constant time]
    c. Find --> 𝛼(𝑛)
    d. Get Component Size --> 𝛼(𝑛)
    e. Check if Connected --> 𝛼(𝑛)
    f. Count Components --> O(1)

**Union Opeartion** (No Path Compression)

    a. Find the roots of the two sets:

        For each element, perform the Find operation to find the root or representative element of the set it belongs to.
        The root element represents the entire set.
    
    b. Merge the sets:

        Determine which set has a larger rank (or depth). The rank is a measure of the height of the set's tree-like structure, where a smaller rank indicates a shallower tree.
        Attach the root of the set with the smaller rank to the root of the set with the larger rank. This ensures that the resulting merged set has a balanced tree structure.
        Update the parent pointer of the root with the smaller rank to point to the root with the larger rank.
        Note: The rank of a set is initially assigned as 0 for each individual element. It increases when two sets with the same rank are merged. The rank of the resulting 
        merged set becomes the maximum of the two ranks plus one.

    c. Adjust the rank if necessary:

        After the merge, check if the ranks of the merged sets are equal. If they are, increment the rank of the resulting merged set by one.
        This adjustment helps maintain a balanced tree structure and ensures that the height of the tree does not increase significantly during subsequent operations.

**Union Opeartion** (Path Compression)

    In the case of path compression in the Union-Find data structure, the Find operation is enhanced to optimize subsequent Find operations, 
    reducing the path length and improving overall performance. When path compression is applied, the steps of the Union operation remain 
    the same, but the Find operation is modified as follows:
    
    a. Find the roots of the two sets:
    Start by performing the Find operation as usual to find the root or representative element of the set that a specific element belongs to.
    Along the path to the root, update the parent pointers of each traversed element to directly point to the root.
    This path compression technique ensures that subsequent Find operations on the same element or other elements in the same set have shorter paths to traverse.
