"""
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

import typing


class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def rotateRight(head, k: int):
    """Turn the list into a circle, then break the circle"""

    if not head:
        return None

    size, tail = 1, head
    while tail.next:
        tail = tail.next
        size += 1

    tail.next = head  # now we have a circular list

    rotate = k % size
    if rotate == 0:
        tail.next = None
        return head

    # get the node before the rotate position
    temp = head
    for _ in range(size - rotate - 1):
        temp = temp.next

    head = temp.next
    temp.next = None
    return head


head = Node(1)
# head.next = Node(1)
# head.next.next = Node(2)

print(rotateRight(head, 0).val)
