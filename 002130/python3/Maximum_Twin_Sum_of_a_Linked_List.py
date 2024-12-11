from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
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
        
        result = 0
        tail = prev
        while head and tail:
            result = max(result, head.val + tail.val)
            head = head.next
            tail = tail.next
        return result
