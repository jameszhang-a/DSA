"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        BFS
        """
        if root is None:
            return 0

        global_max = 0

        def recur(node):
            """
            - update the global max if left + right branch is larger
            - return max(left, right) to be sent upwards
            """
            if node is None:
                # base case: at leaf node
                return 0

            left_branch = recur(node.left)
            right_branch = recur(node.right)

            nonlocal global_max
            global_max = max(global_max, left_branch + right_branch)
            return max(left_branch, right_branch) + 1

        recur(root)
        return global_max
