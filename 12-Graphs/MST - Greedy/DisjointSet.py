class DisjointSet:

    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {i:i for i in self.vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, val):
        if self.parent[val] == val:
            return val
        else: # Suppose parent = {"A":"A", "B":"A", "C":"B", "D":"C"} and you call find("D"). So, D belongs to A as we recurse.
            return self.find(self.parent[val])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
