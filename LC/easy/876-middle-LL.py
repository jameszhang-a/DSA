class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(node):
        li = []
        while(node is not None):
            li.append(node.val)
            node = node.next
        print(li)


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        location = {}
        idx = 0

        while(temp):
            location[idx] = temp
            idx += 1
            temp = temp.next

        return location[len(location)//2]

    def middleNode2(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
n1.next.next.next.next.next = ListNode(6)

n1.print_list()
a = Solution()

ListNode.print_list(a.middleNode(n1))
ListNode.print_list(a.middleNode2(n1))