from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        nxt = None
        while stack:
            curr = stack.pop()
            curr.next = nxt
            nxt = curr
        return nxt
