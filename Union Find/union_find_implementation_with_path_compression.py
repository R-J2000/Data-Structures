# UNION FIND WITH PATH COMPRESSION (for reference)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize each element as its own parent
        self.rank = [0] * n  # Initialize ranks for each element (initially all 0)

    def find(self, x):
        if self.parent[x] != x:  # If x is not the parent of itself (not a root)
            return self.find(self.parent[x])  # Recursively find the root and compress the path
        return x  # Return the root element (representative)

    def union(self, x, y):
        root_x = self.find(x)  # Find the root of x
        root_y = self.find(y)  # Find the root of y

        if root_x == root_y:  # If the elements are already in the same set
            return

        if self.rank[root_x] < self.rank[root_y]:  # If root_x has a smaller rank
            self.parent[root_x] = root_y  # Attach root_x to root_y
        elif self.rank[root_x] > self.rank[root_y]:  # If root_y has a smaller rank
            self.parent[root_y] = root_x  # Attach root_y to root_x
        else:  # If both roots have the same rank
            self.parent[root_y] = root_x  # Attach root_y to root_x
            self.rank[root_x] += 1  # Increment the rank of root_x
