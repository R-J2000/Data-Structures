# FENWICK TREE IMPLEMENTATION (for reference)

class FenwickTree:
    def __init__(self, size):
        """
        Initialize the Fenwick tree with a given size.

        Args:
            size (int): The size of the Fenwick tree.
        """
        self.size = size
        self.tree = [0] * (size + 1)  # Initialize the tree with zeros

    def update(self, index, value):
        """
        Update the element at the given index with the specified value.

        Args:
            index (int): The index of the element to update.
            value (int): The new value to assign to the element.
        """
        while index <= self.size:
            self.tree[index] += value  # Add the value to the current element
            index += index & -index  # Move to the next index

    def get_prefix_sum(self, index):
        """
        Compute the prefix sum up to the given index.

        Args:
            index (int): The index up to which the prefix sum should be computed.

        Returns:
            int: The prefix sum up to the given index.
        """
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.tree[index]  # Add the current element to the sum
            index -= index & -index  # Move to the previous index
        return prefix_sum

    def get_range_sum(self, start_index, end_index):
        """
        Compute the sum of elements within the specified range.

        Args:
            start_index (int): The starting index of the range.
            end_index (int): The ending index of the range.

        Returns:
            int: The sum of elements within the range [start_index, end_index].
        """
        range_sum = self.get_prefix_sum(end_index) - self.get_prefix_sum(start_index - 1)
        return range_sum
