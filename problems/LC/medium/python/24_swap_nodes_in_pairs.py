from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class sol:
    def swapPairs(self, head):

        dummy = ListNode(-1, head)
        prev, curr_node = dummy, head

        while curr_node and curr_node.next:
            # initializing swap nodes
            next_node = curr_node.next

            # swap two nodes
            curr_node.next = next_node.next
            next_node.next = curr_node

            # connect previous pair to newly swapped pair
            prev.next = next_node
            prev = curr_node
            curr_node = curr_node.next

        return dummy.next

    def print(self, head):
        while head:
            print(head.val)
            head = head.next


ans = sol()


input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# ans.print(input)
ans.print(ans.swapPairs(input))
