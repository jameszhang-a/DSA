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

    def in_order(self, root):
        """Traverses the tree in order:
        Left - Middle - Right
        """
        if root is None:
            return

        self.in_order(root.left)
        print(root)
        self.in_order(root.right)

    def pre_order(self, root):
        """Traverses the tree in order:
        Middle - Left - Right
        """
        if root is None:
            return

        print(root)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        """Traverses the tree in order:
        Left - Right - Middle
        """
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root)

    def leaf_only(self, root):
        if root is None:
            return

        if self.is_leaf(root):
            print(f"{root} is leaf")

        self.leaf_only(root.left)
        self.leaf_only(root.right)

    def is_leaf(self, root):
        if root is None:
            return False

        if (root.left and root.right) is None:
            return True
        return False

    def level_order(self, root):
        """Same thing as BFS basically"""
        queue = [root]

        while queue:
            curr = queue.pop(0)
            print(curr)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

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
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.print2D()

    print("InOrder")
    bst.in_order(bst.root)

    print("PreOrder:")
    bst.pre_order(bst.root)

    print("PostOrder:")
    bst.post_order(bst.root)

    print("Leaf Only:")
    bst.leaf_only(bst.root)

    print("Level Order:")
    bst.level_order(bst.root)

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
