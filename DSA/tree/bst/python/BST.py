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

    def in_order(self, root, list=None):
        """Traverses the tree in order:
        Left - Middle - Right
        """
        if root is None:
            return

        if list is None:
            list = []

        self.in_order(root.left, list)
        list.append(root.val)
        self.in_order(root.right, list)

        return list

    def pre_order(self, root, list=None):
        """Traverses the tree in order:
        Middle - Left - Right
        """
        if root is None:
            return

        if list is None:
            list = []

        list.append(root.val)
        self.pre_order(root.left, list)
        self.pre_order(root.right, list)

        return list

    def post_order(self, root, list=None):
        """Traverses the tree in order:
        Left - Right - Middle
        """
        if root is None:
            return

        if list is None:
            list = []

        self.post_order(root.left, list)
        self.post_order(root.right, list)
        list.append(root.val)

        return list

    def leaf_only(self, root, list=None):
        if root is None:
            return

        if list is None:
            list = []

        if self.is_leaf(root):
            list.append(root.val)

        self.leaf_only(root.left, list)
        self.leaf_only(root.right, list)
        return list

    def is_leaf(self, root):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return True
        return False

    def level_order(self, root):
        """Same thing as BFS basically"""
        queue = [root]
        visited = []

        while queue:
            curr = queue.pop(0)
            visited.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return visited

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


if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    # bst.insert(2)
    bst.insert(4)
    # bst.insert(7)
    bst.insert(9)
    bst.print2D()

    print("InOrder")
    print(bst.in_order(bst.root), "\n")

    print("PreOrder:")
    print(bst.pre_order(bst.root), "\n")

    print("PostOrder:")
    print(bst.post_order(bst.root), "\n")

    print("Leaf Only:")
    print(bst.leaf_only(bst.root), "\n")

    print("Level Order:")
    print(bst.level_order(bst.root), "\n")

"""
const tree = new BST();
const node1 = new Node(5);
const node2 = new Node(3);
const node3 = new Node(8);

tree.insert(5);
tree.insert(3);
tree.insert(8);
tree.insert(2);
tree.insert(4);
tree.insert(7);
tree.insert(9);

/**
 *      5
 *   3      8
 *  2  4   7  9
 */

console.log(tree.contains(-1));
tree.print2D(tree.root);

// console.log('In-Order: ');
// tree.inOrder(tree.root);

// console.log('Pre-Order: ');
// tree.preOrder(tree.root);

// console.log('Post-Order: ');
// tree.postOrder(tree.root);

console.log(`Min ${tree.findMin()}`);
console.log(`Max ${tree.findMax()}`);
"""
