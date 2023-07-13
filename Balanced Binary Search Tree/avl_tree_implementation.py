# IMPLEMENTATION OF AVL TREE (for reference)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a key into the AVL tree.

        Args:
            key: The key to be inserted.
        """
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Recursive helper function for inserting a key into the AVL tree.

        Args:
            node: The current node being considered.
            key: The key to be inserted.

        Returns:
            The updated node after insertion.
        """
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Perform rotations if necessary
        if balance > 1:  # Left subtree is taller
            if key < node.left.key:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:  # Right subtree is taller
            if key > node.right.key:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        
        return node

    def delete(self, key):
        """
        Delete a key from the AVL tree.

        Args:
            key: The key to be deleted.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """
        Recursive helper function for deleting a key from the AVL tree.

        Args:
            node: The current node being considered.
            key: The key to be deleted.

        Returns:
            The updated node after deletion.
        """
        if not node:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to be deleted found

            # Case 1: Node has no children or only one child
            if not node.left or not node.right:
                if node.left:
                    return node.left
                else:
                    return node.right
            # Case 2: Node has two children
            else:
                successor = self._get_min_value_node(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Perform rotations if necessary
        if balance > 1:  # Left subtree is taller
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        if balance < -1:  # Right subtree is taller
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        
        return node

    def _left_rotate(self, z):
        """
        Perform a left rotation.

        Args:
            z: The node at which the rotation is performed.

        Returns:
            The new root after rotation.
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """
        Perform a right rotation.

        Args:
            z: The node at which the rotation is performed.

        Returns:
            The new root after rotation.
        """
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        """
        Get the height of a node.

        Args:
            node: The node to get the height of.

        Returns:
            The height of the node.
        """
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """
        Get the balance factor of a node.

        Args:
            node: The node to get the balance factor of.

        Returns:
            The balance factor of the node.
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_min_value_node(self, node):
        """
        Get the node with the minimum value in the given subtree.

        Args:
            node: The root node of the subtree.

        Returns:
            The node with the minimum value.
        """
        current = node
        while current.left:
            current = current.left
        return current
