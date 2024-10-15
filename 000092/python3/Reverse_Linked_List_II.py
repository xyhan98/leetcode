from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        node = dummy
        i = 0
        while i < left - 1:
            node = node.next
            i += 1
        node.next = self.reverse(node.next, right - left + 1)
        return dummy.next

    def reverse(self, head: ListNode, num: int) -> ListNode:
        prev = None
        curr = head
        i = 0
        while i < num:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
        head.next = curr
        return prev
