"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postOrder(root):
            if not root:
                return 0

            leftHeight = postOrder(root.left)
            rightHeight = postOrder(root.right)

            if abs(leftHeight - rightHeight) > 1:
                raise Exception("not balanced")

            return max(leftHeight, rightHeight) + 1

        try:
            postOrder(root)
            return True
        except:
            return False


t1 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
t2 = TreeNode(2, TreeNode(1), TreeNode(3))
t3 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
t4 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.isBalanced(t1))
print(sol.isBalanced(t2))
print(sol.isBalanced(t3))
print(sol.isBalanced(t4))
