from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(p: Optional[ListNode], q: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if p is None and q is None:
                return None if carry == 0 else ListNode(carry)
            val = carry
            if p is not None:
                val += p.val
                p = p.next
            if q is not None:
                val += q.val
                q = q.next
            carry = val // 10
            val = val % 10
            return ListNode(val, dfs(p, q, carry))

        return dfs(l1, l2, 0)
