"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.



Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you
need to find the kth smallest frequently, how would you optimize?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right


from collections import deque
from typing import List, Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: List[TreeNode] = []
        i = 1
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            # now root is none and stack has first left node
            curr = stack.pop()
            if i == k:
                return curr.val
            i += 1
            root = curr.right


t1 = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
t2 = TreeNode(2, TreeNode(1), TreeNode(3))

sol = Solution()
print(sol.kthSmallest(t1, 0))
print(sol.kthSmallest(t2, 0))
