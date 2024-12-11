from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = ListNode()
        node = dummy
        carry = 0

        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            node.next = ListNode(carry)
        
        return reverse(dummy.next)
