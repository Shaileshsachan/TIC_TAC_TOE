from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def dfsutil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsutil(neighbour, visited)

    def dfs(self):
        visited = set()

        for vertex in list(self.graph):
            if vertex not in visited:
                self.dfsutil(vertex, visited)


g = Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)

print(f"Following is Depth First Search Traversal")
g.dfs()
