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
        # Visit first node
        visited = [start]
        to_visit = deque([start])

        while to_visit:
            curr = to_visit.popleft()
            print(curr)

            if curr in self.dict:
                # Add each of its unvisited adjencents
                for edge in self.dict[curr]:
                    if edge not in visited:
                        visited.append(edge)
                        to_visit.append(edge)

    def DFS(self, start):
        print(start)

        self.DFS(x)


customGraph = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
}

graph = Graph(customGraph)
graph.BFS("a")
