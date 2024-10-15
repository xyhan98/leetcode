from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nxt = self.deleteDuplicates(head.next)
        head.next = nxt
        if not nxt or head.val != nxt.val:
            return head
        return nxt
