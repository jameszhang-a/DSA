"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should
work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.



Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


from collections import deque
from turtle import right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        q = deque([root])
        visited = []

        while q:
            curr = q.popleft()
            visited.append(str(curr.val if curr else "x"))

            if curr is None:
                continue

            q.append(curr.left)
            q.append(curr.right)

        return ",".join(visited)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data[0] == "x":
            return None

        data = data.split(",")

        head = TreeNode(data[0])
        # temp = [head]

        q = deque([head])
        i = 1
        while q and i < len(data) - 1:
            curr = q.popleft()

            val = data[i]
            if val != "x":
                left = TreeNode(val)
                curr.left = left
                q.append(left)
            i += 1

            val = data[i]
            if val != "x":
                right = TreeNode(val)
                curr.right = right
                q.append(right)
            i += 1

        return head

        # for i in range(len(data)):
        #     if data[i] == "x" or temp[i] is None:
        #         continue

        #     root = temp[i]
        #     if (j := self.leftChild(i)) < len(data):
        #         if data[j] == "x":
        #             root.left = None
        #             temp.append(None)
        #         else:
        #             root.left = TreeNode(data[j])
        #             temp.append(root.left)

        #     if (j := self.rightChild(i)) < len(data):
        #         if data[j] == "x":
        #             root.right = None
        #             temp.append(None)
        #         else:
        #             root.right = TreeNode(data[j])
        #             temp.append(root.right)

        return head


# Your Codec object will be instantiated and called as such:
# BST = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
# BST = TreeNode(1, TreeNode(2))
BST = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)))

ser = Codec()
serialized = ser.serialize(BST)
print(serialized)
deser = Codec()
ans = deser.deserialize(serialized)
print(ans)
print(ser.serialize(ans))
