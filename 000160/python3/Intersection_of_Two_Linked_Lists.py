from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node = headA
        while node:
            setattr(node, "visited", True)
            node = node.next
        node = headB
        while node:
            try:
                getattr(node, "visited")
                return node
            except:
                node = node.next
        return None
