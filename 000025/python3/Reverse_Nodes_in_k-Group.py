from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, node = None, head
        for _ in range(k):
            if node is None:
                return head
            prev = node
            node = node.next
        prev.next = None
        prev = self.reverseKGroup(node, k)
        return self.reverse(prev, head)

    def reverse(self, prev: Optional[ListNode], curr: ListNode) -> ListNode:
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
