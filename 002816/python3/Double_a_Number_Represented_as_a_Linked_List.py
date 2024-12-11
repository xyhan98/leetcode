from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(prev: Optional[ListNode], curr: ListNode) -> ListNode:
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = reverse(None, head)
        carry = 0
        prev, curr = None, head
        while curr:
            val = curr.val * 2 + carry
            carry = val // 10
            curr.val = val % 10
            prev = curr
            curr = curr.next
        if carry > 0:
            prev.next = ListNode(carry)
        return reverse(None, head)
