from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


def top_sort(g):
    graph = g.graph
    order = [0] * g.vertices
    visited = []
    queue = []

    # First create a inorder list
    for i in range(g.vertices):
        for to in graph[i]:
            order[to] += 1
    print(order)

    for i, n in enumerate(order):
        if n == 0:
            queue.append(i)

    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        for to in graph[curr]:
            order[to] -= 1
            if order[to] == 0:
                queue.append(to)
    print(f"order: {visited}")


# Testing
myGraph = Graph(5)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)

print("Topological Sort")
top_sort(myGraph)
