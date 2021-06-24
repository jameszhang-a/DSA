# Definition for singly-linked list.
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # node1 = l1.next
        # node2 = l2.next
        fin_list = None

        while l1 or l2:
            if not fin_list:
                if l1 and not l2:
                    return l1
                if l2 and not l1:
                    return l2
                if not (l1 and l2):
                    return fin_list
                
                if l1.val < l2.val:
                    fin_list = ListNode(l1.val)
                    l1 = l1.next
                else:
                    fin_list = ListNode(l2.val)
                    l2 = l2.next
                temp = fin_list
                continue

            if l1 and l2 and l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l1 and l2 and l2.val <= l1.val:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            elif not l1:
                temp.next = l2
                return fin_list 
            elif not l2:
                temp.next = l1
                return fin_list
            
            temp = temp.next

        return fin_list


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
ListNode.print_list(sol.mergeTwoLists(n1, n2))
