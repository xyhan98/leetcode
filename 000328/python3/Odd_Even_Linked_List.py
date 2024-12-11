from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(), ListNode()
        o, e = odd, even
        while head and head.next:
            o.next = head
            o = o.next
            e.next = head.next
            e = e.next
            head = head.next.next
        if head:
            o.next = head
            o = o.next
        e.next = None
        o.next = even.next
        return odd.next
