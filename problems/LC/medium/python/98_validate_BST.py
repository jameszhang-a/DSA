"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
from curses.ascii import SO
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order traversal
        # check if ≥ on each new value

        # recursive approach, dumb, stupid
        """
        def inorder(root, order=[]):
            if root is None:
                return order

            order = inorder(root.left)
            order.append(root.val)
            order = inorder(root.right)
            return order

        order = inorder(root)
        last = order[0]
        for val in range(1, len(order)):
            if order[val] <= last:
                return False

            last = order[val]

        return True
        """
        order = []
        stack = []
        while root or stack:
            # get to the left most node while adding roots to stack
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if order and root.val <= order[-1]:
                return False

            order.append(root.val)
            root = root.right

        return True


t1 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))  # false
t2 = TreeNode(2, TreeNode(1), TreeNode(3))  # true

sol = Solution()
print(sol.isValidBST(t1))
print(sol.isValidBST(t2))
