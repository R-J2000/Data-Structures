**Implementation Details**

No Path Compression

The UnionFind class represents the Union-Find data structure. The parent list is initialized, where each element is initially its own parent.
The find method iteratively traverses up the parent chain until it finds the root (the element whose parent is itself). It returns the root element, which represents the set.
The union method finds the roots of the given elements using the find method. If the roots are different, it attaches the root of one set to the root of the other set by updating the parent pointer.

Path Compression

The UnionFind class represents the Union-Find data structure. It initializes the parent list, where each element is initially its own parent, and the rank list, where initially all ranks are 0.
The find method is used to find the root (representative) of an element. If an element is not its own parent, indicating that it is not the root, the method recursively finds the root and compresses the path by updating the parent pointers of all traversed elements to directly point to the root. Finally, it returns the root element.
The union method is used to merge two sets. It finds the roots of the given elements using the find method. If the roots are different, the method compares the ranks of the roots. If one root has a smaller rank, it becomes a child of the other root. If both roots have the same rank, one root becomes the child of the other, and the rank of the new parent is incremented.
