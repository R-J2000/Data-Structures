# UNION FIND WITHOUT PATH COMPRESSION (for reference)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize each element as its own parent

    def find(self, x):
        while x != self.parent[x]:  # Traverse up the parent chain until finding the root
            x = self.parent[x]
        return x  # Return the root element (representative)

    def union(self, x, y):
        root_x = self.find(x)  # Find the root of x
        root_y = self.find(y)  # Find the root of y

        if root_x != root_y:  # If the elements are not already in the same set
            self.parent[root_x] = root_y  # Attach root_x to root_y
