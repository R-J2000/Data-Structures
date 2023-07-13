#### Balanced Binary Search Tree

A balanced binary search tree is a type of binary search tree (BST) that automatically maintains balance to ensure efficient search, insertion, and deletion operations. It achieves this balance by dynamically adjusting the tree structure as elements are added or removed.

In a balanced BST, such as an AVL tree, red-black tree, or B-tree, the height of the left and right subtrees of any node differs by at most a constant factor. This balanced structure ensures that the tree remains relatively shallow, resulting in efficient average-case time complexity for operations.

Operation Cost

    a. Insert --> O(log(n)) 
    b. Delete --> O(log(n)) 
    c. Remove --> O(log(n)) 
    d. Search --> O(log(n)) 
    
**Rotations**

Right Rotation

    A right rotation is performed on a node to move it down the tree and promote its left child as the new root of the subtree. This 
        operation helps balance the tree by adjusting the structure when the left subtree becomes taller than the right subtree.

    The steps to perform a right rotation are as follows:

        a. Let x be the node to rotate, and y be its left child.
        b. Assign the right child of y as the left child of x.
        c. Assign y as the parent of x.
        d. Update the parent of x to be y's parent.
        e. Update the parent reference of y to point to x.
        
Example:
    
        x                     y
       / \                   / \
      y   T3      -->       T1  x
     / \                       / \
    T1  T2                    T2  T3    



Left Rotation

    A left rotation is the reverse of a right rotation. It moves a node down the tree and promotes its right child as the new root of the 
        subtree. This operation helps balance the tree when the right subtree becomes taller than the left subtree.

    The steps to perform a left rotation are as follows:

        a. Let x be the node to rotate, and y be its right child.
        b. Assign the left child of y as the right child of x.
        c. Assign y as the parent of x.
        d. Update the parent of x to be y's parent.
        e. Update the parent reference of y to point to x.

Example:

        x                     y
       / \                   / \
      T1  y     -->         x   T3
         / \               / \
        T2  T3            T1  T2

#### AVL Trees [See attached Illustrations]

An AVL tree is a type of self-balancing binary search tree (BST) that maintains its balance by ensuring that the heights of the left and right subtrees of any node differ by at most 1. It is named after its inventors, Adelson-Velsky and Landis. The self-balancing property of AVL trees helps guarantee efficient search, insertion, and deletion operations with a worst-case time complexity of O(log n), where n is the number of nodes in the tree.

The key features of an AVL tree are as follows:

    a. Balancing Condition: In an AVL tree, for every node, the heights of its left and right subtrees differ by at most 1. This balance 
        condition ensures that the tree remains relatively shallow, providing efficient search and insertion operations.

    b. Height-Balanced Structure: AVL trees maintain a balanced structure by performing rotations to restore balance whenever it is violated 
        during insertions or deletions. The rotations adjust the tree's structure to maintain the balance condition while preserving the BST 
        property.

    c. Balancing Rotations: AVL trees use four types of rotations to restore balance: [See attached Illustrations]

        i. Left Rotation: Performed when the right subtree of a node becomes taller.
        ii. Right Rotation: Performed when the left subtree of a node becomes taller.
        iii. Left-Right Rotation (LR Rotation): Performed when the left subtree of a node is taller and its right subtree is taller than 
            its left subtree.
        iv. Right-Left Rotation (RL Rotation): Performed when the right subtree of a node is taller and its left subtree is taller than 
            its right subtree.
            
    d. Efficient Operations: Due to the self-balancing nature of AVL trees, operations like search, insertion, and deletion have a worst-case 
        time complexity of O(log n). This makes AVL trees suitable for scenarios where efficient data retrieval and modification are crucial.

The AVL tree ensures that the heights of the subtrees remain balanced, preventing degeneration into a linked list-like structure. However, the maintenance of balance comes with the cost of additional bookkeeping during insertion and deletion operations.

While AVL trees provide excellent balance guarantees, they require additional overhead in terms of memory and extra computation for maintaining balance. For applications with frequent insertions and deletions but less stringent balance requirements, other self-balancing trees like red-black trees may be preferred.

**Removal from BST Tree**

    When removing a value from an AVL tree, the process involves finding and deleting the corresponding node, and then restoring the 
        balance of the tree to maintain the AVL property. There are four possible cases to consider when removing a node from an AVL tree:

        Case 1: Node to be deleted is a leaf node (no children):
            In this case, the node to be deleted is a leaf node, meaning it has no children. To remove the node, simply remove its 
            reference from its parent, and the tree remains balanced.

        Case 2: Node to be deleted has one child:
            When the node to be deleted has only one child, the process is straightforward. Replace the node with its child, adjusting 
            the parent's reference accordingly. The tree remains balanced in this case as well.

        Case 3: Node to be deleted has two children:
            When the node to be deleted has two children, the process is more involved. The idea is to replace the node with its 
            inorder predecessor or inorder successor, which are the closest nodes in value to the node being deleted.

                a. Using the Inorder Predecessor:
                    i. Find the inorder predecessor (the largest node in the left subtree) of the node to be deleted.
                    ii. Replace the node to be deleted with its inorder predecessor.
                    iii. Recursively delete the inorder predecessor from the left subtree.

                b. Using the Inorder Successor:
                    i. Find the inorder successor (the smallest node in the right subtree) of the node to be deleted.
                    ii. Replace the node to be deleted with its inorder successor.
                    iii. Recursively delete the inorder successor from the right subtree.

    After deleting the inorder predecessor or successor, the tree may become unbalanced, so additional steps are needed to restore balance.
