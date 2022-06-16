class TreeNode:
    """
    run: export PYTHONPATH="${PYTHONPATH}:/Users/james/code/learn/coding-problems"
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)


def deserialize(string):
    if string == "{}":
        return None

    nodes = [
        None if val == "null" else TreeNode(int(val))
        for val in string.replace(" ", "").strip("[]{}").split(",")
    ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align="center", font=("Arial", 12, "bold"))
            draw(node.left, x - dx, y - 60, dx / 1.7)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 1.7)

    import turtle

    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, h**3)
    t.hideturtle()
    turtle.mainloop()


if __name__ == "__main__":
    # drawtree(deserialize("[1,2,3,null,null,4,null,null,5]"))
    # drawtree(deserialize("[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]"))
    drawtree(
        deserialize(
            "[17, 12, null, null, 934, 49, null, 584, 552, 551, 460, 372, 86, null, 122, 123, 456, 437, null, 440, null, null, 507, null, 541, null, null, null, null, 658, 627, null, null, 788, 725, null, null, 857, null, null, 936, null, null]"
        )
    )
