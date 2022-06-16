"""
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value.
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.



Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2

Example 2:
Input: root = [1,4,5,4,4,5]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def recur(root):
            if root is None:
                return 0, None

            l_len, l_val = recur(root.left)
            r_len, r_val = recur(root.right)

            nonlocal longest

            if l_val == root.val == r_val:
                longest = max(longest, l_len + r_len)
                return max(l_len, r_len) + 1, root.val
            elif l_val == root.val:
                longest = max(longest, l_len)
                return l_len + 1, root.val
            elif r_val == root.val:
                longest = max(longest, r_len)
                return r_len + 1, root.val
            else:
                return 1, root.val

        recur(root)
        return longest


tree = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
tree2 = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))
s = Solution()

print(s.longestUnivaluePath(tree))
print(s.longestUnivaluePath(tree2))
