from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        n1, n2 = head, prev
        node = dummy
        while n1 and n2:
            node.next = n1
            n1 = n1.next
            node = node.next
            node.next = n2
            n2 = n2.next
            node = node.next
        if n1:
            node.next = n1
        else:
            node.next = n2
