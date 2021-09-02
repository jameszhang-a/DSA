class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)


class Tree:
    COUNT = 5

    def __init__(self) -> None:
        self.root = None
    