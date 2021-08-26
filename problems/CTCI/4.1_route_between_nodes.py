class Node:
    def __init__(self, val: int, children: list = None) -> None:
        self.val = val
        self.visited = False
        self.children = []

    def addChild(self, child) -> None:
        self.children = [*self.children, *child]


class Graph:
    def __init__(self, graph: list = None) -> None:
        self.graph = graph

    def connected(self, start, end) -> bool:
        """Using BFS for easier time"""

        queue = [start]
        start.visited = True

        while queue:
            curr = queue.pop(0)
            if curr == end:
                return True

            for child in curr.children:
                if not child.visited:
                    queue.append(child)
                    child.visited = True

        return False


def is_connected(graph, a, b):
    return graph.connected(a, b)


nodeA = Node("a")
nodeB = Node("b")
nodeC = Node("c")
nodeD = Node("d")
nodeE = Node("e")
nodeF = Node("f")

nodeA.addChild([nodeB, nodeC])
nodeB.addChild([nodeA, nodeD, nodeE])
nodeC.addChild([nodeA, nodeE])
nodeD.addChild([nodeB, nodeE, nodeF])
nodeE.addChild([nodeD, nodeF, nodeC])
nodeF.addChild([nodeD, nodeE])

graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeF])

print(is_connected(graph, nodeA, nodeF))
