"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(node):
        li = []
        while node is not None:
            li.append(node.val)
            node = node.next
        print(li)


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        head = result
        while list1 and list2:
            if list1.val >= list2.val:
                result.next = list2
                list2 = list2.next

            elif list1.val < list2.val:
                result.next = list1
                list1 = list1.next

            result = result.next
        result.next = list1 or list2
        return head.next


n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(4)
n1.next.next.next = ListNode(7)
n1.next.next.next.next = ListNode(9)
# n1.next.next.next = ListNode(8)
ListNode.print_list(n1)

n2 = ListNode(1)
n2.next = ListNode(3)
n2.next.next = ListNode(4)
# n2.next.next.next = ListNode(8)
ListNode.print_list(n2)

sol = Solution()
ListNode.print_list(sol.mergeTwoLists(n1, n2))  # want 1, 1, 2, 3, 4, 4, 7, 9
