#### Binary Search Tree
[See Attached Pictures]

**Binary Tree** - A binary tree is a type of data structure in which each node can have at most two children, referred to as the left child and the right child. It is a recursive data structure where each node in the tree represents an element, and the connections between nodes represent the relationships between those elements.

The structure of a binary tree can be visualized as a collection of nodes connected by edges. The topmost node in the tree is called the root node, and from there, each node can have a left child, a right child, or both. The nodes without any children are known as leaf nodes or external nodes. The path from the root to any leaf node forms a unique sequence of nodes, also known as a path or a branch. [See Attached Pictures]

**Binary Search Tree** - Binary search trees (BSTs) are a type of data structure used for efficient searching, insertion, and deletion operations on a collection of elements. They are organized in a hierarchical manner, where each element in the tree has at most two children, referred to as the left child and the right child. 

The structure of a binary search tree follows a specific property known as the BST invariant: for any node in the tree, all elements in its left subtree are smaller than the node's value, and all elements in its right subtree are greater than the node's value. This property allows for efficient searching and retrieval of elements within the tree.

The key advantage of binary search trees is their ability to perform search operations with a time complexity of O(log n), on average, where n is the number of elements in the tree. This efficiency is achieved by recursively dividing the search space in half at each step, based on the comparison of the target value with the current node.

Use Cases:

    a. Implementation of some map and set ADTs
    b. Red Black Trees
    c. AVL Trees
    d. Implementation of binary heap
    
Operation Cost:

    a. Insert --> O(n) [O(log(n)) on average]
    b. Delete --> O(n) [O(log(n)) on average]
    c. Remove --> O(n) [O(log(n)) on average]
    d. Search --> O(n) [O(log(n)) on average]
    
**Insertion and Removal in Binary Search Trees**

Insertion in a Binary Search Tree:

    To insert a new element into a BST, we compare the value of the new element with each node starting from the root and follow these steps:
        a. If the tree is empty, we create a new node and make it the root.
        b. If the value of the new element is less than the current node's value, we move to the left subtree.
        c. If the value is greater than the current node's value, we move to the right subtree.
        d. We repeat these steps recursively until we find an appropriate position to insert the new element as a leaf node.
        e. If the value is already present in the tree, it can be handled in different ways based on the specific implementation. 
            It can either be ignored or inserted as a duplicate, depending on the requirements.
            
    The insertion process ensures that the binary search tree property is maintained, with smaller elements on the left and larger 
        elements on the right of each node.

Removal in a Binary Search Tree:

    Removing an element from a BST involves finding the node containing the target element and handling different cases:
        a. If the node to be removed is a leaf node (has no children), it can be directly removed from the tree by 
            updating its parent's reference to null.
        b. If the node has only one child, we replace the node with its child by adjusting the appropriate references.
        c. If the node has two children, we have to find either its in-order predecessor (the largest element in the left subtree) or 
            its in-order successor (the smallest element in the right subtree) to replace the node. Once found, we replace the node's 
            value with the predecessor/successor value and then remove the predecessor/successor node using one of the above cases.
            
    After performing removal, we need to ensure that the binary search tree property is maintained throughout the tree.

    
**Binary Search Trees Traversal**

Sample Tree:

          4
        /   \
       2     6
      / \   / \
     1   3 5   7

Preorder Traversal:

    In a preorder traversal, the nodes are visited in the order: root, left subtree, right subtree. It follows the recursive approach:
        a. Visit the root node.
        b. Traverse the left subtree using a recursive call to preorder traversal.
        c. Traverse the right subtree using a recursive call to preorder traversal.
    Preorder traversal is useful for creating a copy of the tree, prefix expression evaluation, and extracting prefix expressions from the tree.
    
    The preorder traversal of the sample tree will be: 4, 2, 1, 3, 6, 5, 7.

In-order Traversal:

    In an in-order traversal, the nodes are visited in the order: left subtree, root, right subtree. It follows the recursive approach:
    Traverse the left subtree using a recursive call to in-order traversal.
        a. Visit the root node.
        b. Traverse the right subtree using a recursive call to in-order traversal.
        c. In-order traversal of a binary search tree produces the elements in sorted order. It is commonly used for getting a sorted list of 
    elements from the tree, binary search tree validation, and expression evaluation (in case of arithmetic expressions).
    
    The in-order traversal of the sample tree will be: 4, 2, 1, 3, 6, 5, 7.

Postorder Traversal:

    In a postorder traversal, the nodes are visited in the order: left subtree, right subtree, root. It follows the recursive approach:
        a. Traverse the left subtree using a recursive call to postorder traversal.
        b. Traverse the right subtree using a recursive call to postorder traversal.
        c. Visit the root node.
    Postorder traversal is often used in deleting a binary tree, evaluating postfix expressions, and collecting post-order expressions from the tree.
    
    The postorder traversal of the sample tree will be: 4, 2, 1, 3, 6, 5, 7.

Level Order Traversal:

    Level order traversal, also known as breadth-first traversal, visits the nodes in each level from left to right. 
    It visits the nodes level by level, starting from the root and moving to subsequent levels. 
    It uses a queue data structure to process nodes in a breadth-first manner.
        a. Enqueue the root node into a queue.
        b. While the queue is not empty, dequeue a node and visit it.
        c. Enqueue the left child and right child (if they exist) of the dequeued node.
    Level order traversal is commonly used for tree-level specific operations, level order insertion, and level order printing.
    
    The level order traversal of the sample tree will be: 4, 2, 1, 3, 6, 5, 7.
