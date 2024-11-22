from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-9999)
        setattr(dummy, "prev", None)
        tail = ListNode(val=9999)
        setattr(tail, "prev", dummy)
        dummy.next = tail
        while head is not None:
            node = head.next
            t = tail
            while head.val < t.val:
                t = t.prev
            head.next = t.next
            t.next = head
            setattr(head, "prev", t)
            head.next.prev = head
            head = node
        
        tail.prev.next = None
        return dummy.next
