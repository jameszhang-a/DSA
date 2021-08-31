"""
Given a binary tree, return a list of strings containing all root to leaf paths. 

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
"""


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)


class BST:
    COUNT = 5

    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        ins = Node(val)

        if self.root is None:
            self.root = ins
            return

        self.root = self.insert_help(self.root, ins)

    def insert_help(self, root, ins):
        if root is None:
            return ins

        if ins.val < root.val:
            root.left = self.insert_help(root.left, ins)
        elif ins.val > root.val:
            root.right = self.insert_help(root.right, ins)
        else:
            print("can't insert dups")

        return root

    def print2D(self):
        self.print2DUtil(self.root, 0)

    def print2DUtil(self, root, space):
        if root == None:
            return

        space += self.COUNT

        self.print2DUtil(root.right, space)

        str = ""
        str += "\n"

        for i in range(self.COUNT, space):
            str += "  "

        str = str + f"{root}" + "\n"

        print(str)

        self.print2DUtil(root.left, space)

    def is_leaf(self, root):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return True
        return False

    def find_paths(self, root, path=[], list=[]):
        """
        Finds each path from root to leaf
        """
        path.append(f"{root.val}")

        if root.left:
            self.find_paths(root.left, path, list)
        if root.right:
            self.find_paths(root.right, path, list)

        if self.is_leaf(root):
            # After reaching a leaf, add the current path
            list.append("->".join(path))
            path.pop()
            return

        # Popping the most recent node each time moving back to stack
        path.pop()
        return list


if __name__ == "__main__":
    bst = BST()

    node0 = Node(1)
    node1 = Node(2)
    node2 = Node(3)

    node0.left = node1
    node0.right = node2
    bst.root = node0

    """
    node0 = Node(8)
    node1 = Node(2)
    node2 = Node(29)
    node3 = Node(3)
    node4 = Node(9)

    node0.left = node1
    node0.right = node2
    node2.left = node3
    node2.right = node4
    bst.root = node0
    
    
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    # bst.insert(2)
    bst.insert(4)
    # bst.insert(7)
    bst.insert(9)
    bst.print2D()
    """
    print(bst.find_paths(bst.root))
