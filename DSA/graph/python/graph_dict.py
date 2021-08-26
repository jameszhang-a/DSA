#   Graph represented with dictionary


from collections import deque


class Graph:
    # Using append() and popleft() to implement queue
    from collections import deque

    def __init__(self, dict=None):
        if dict is None:
            self.dict = {}

        self.dict = dict

    def addEdge(self, vertex, edge):
        self.dict[vertex].append(edge)

    def BFS(self, start):
        """Implement BFS with queue structure"""

        # Visit first node
        visited = [start]
        to_visit = deque([start])

        while to_visit:
            curr = to_visit.popleft()
            print(curr)

            if curr in self.dict:
                # Add each of its unvisited adjencents to queue
                for edge in self.dict[curr]:
                    if edge not in visited:
                        visited.append(edge)
                        to_visit.append(edge)

    def DFS(self, start):
        """Implement DFS with stack structure"""

        # Visit first node
        visited = [start]
        to_visit = [start]

        while to_visit:
            # Visit most recent node
            curr = to_visit.pop()
            print(curr)

            # Add unvisited adjencents to stack
            if curr in self.dict:
                for edge in self.dict[curr]:
                    if edge not in visited:
                        visited.append(edge)
                        to_visit.append(edge)


customGraph = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f", "c"],
    "f": ["d", "e"],
}

graph = Graph(customGraph)
print("BFS: ")
graph.BFS("a")

print("DFS: ")
graph.DFS("a")
