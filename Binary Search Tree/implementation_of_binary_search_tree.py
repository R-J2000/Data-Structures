# IMPLEMENTATION OF BINARY SEARCH TREE (for reference)

# Define the Node class for individual nodes in the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define the BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a value into the BST
    def insert(self, value):
        if self.root is None:                     # If the tree is empty, create a root node
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)   # Call the recursive helper function for insertion

    # Recursive helper function for insertion
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:               # If value is less than current node, move to the left
            if current_node.left is None:
                current_node.left = Node(value)      # If left child is None, create a new node
            else:
                self._insert_recursive(current_node.left, value)   # Recursive call on left subtree
        else:                                        # If value is greater than or equal to current node, move to the right
            if current_node.right is None:
                current_node.right = Node(value)     # If right child is None, create a new node
            else:
                self._insert_recursive(current_node.right, value)  # Recursive call on right subtree

    # Method to search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)   # Call the recursive helper function for search

    # Recursive helper function for search
    def _search_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:  # Base cases: value not found or found at current node
            return current_node

        if value < current_node.value:
            return self._search_recursive(current_node.left, value)  # Search in the left subtree
        else:
            return self._search_recursive(current_node.right, value)  # Search in the right subtree

    # Method to perform an in-order traversal of the BST
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)   # Call the recursive helper function for in-order traversal
        return result

    # Recursive helper function for in-order traversal
    def _inorder_recursive(self, current_node, result):
        if current_node is not None:
            self._inorder_recursive(current_node.left, result)   # Traverse left subtree
            result.append(current_node.value)                    # Append current node value
            self._inorder_recursive(current_node.right, result)  # Traverse right subtree
