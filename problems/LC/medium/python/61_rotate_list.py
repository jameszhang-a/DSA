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
    tail, new_tail = head, head
    size = 1
    while tail and tail.next:
        tail = tail.next
        size += 1

    print(f"size of list: {size}")

    # if list is 4, and shift 5, same as shift 1
    offset = k % size
    print(f"Offset is: {offset}")

    # edge case
    if offset == 0:
        return head

    tail_pos = size - offset - 1
    print(f"New tail is at: {tail_pos}")

    for i in range(0, tail_pos):
        new_tail = new_tail.next

    print(tail.val)
    old_head = head
    head = new_tail.next
    new_tail.next = None
    tail.next = old_head

    return head


head = Node(0)
head.next = Node(1)
head.next.next = Node(2)

rotateRight(head, 4)
