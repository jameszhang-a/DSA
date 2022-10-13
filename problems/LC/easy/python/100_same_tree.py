"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:
The number of nodes in both trees is in the range [0, 100].
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        idea is that if both roots exist:
            then the left and right must be the same
        if one of them is None:
            then both have to be None
        """

        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        else:
            return p is None and q is None
