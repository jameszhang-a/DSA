"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”



Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        l, r = min(q.val, p.val), max(q.val, p.val)

        # recursive helper function
        def search(root):
            # base case
            # if l and r are on separates sides of root, the root is ancestor
            if l <= root.val and r >= root.val:
                return root

            # if both are smaller than root, then recur to the left
            if l < root.val and r < root.val:
                return search(root.left)

            # likewise for the right side
            elif l > root.val and r > root.val:
                return search(root.right)

        return search(root)
