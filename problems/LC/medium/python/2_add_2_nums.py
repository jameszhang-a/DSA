from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        while both are not None:
            add two values
            if more than 10
                mod 10
                carry over 1
            add sum to output list
        """

        carry = 0
        dummy = ListNode()
        head = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, rem = divmod(val1 + val2 + carry, 10)

            head.next = ListNode(rem)
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


sol = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

ans = sol.addTwoNumbers(l1, l2)

sol.print_list(ans)
