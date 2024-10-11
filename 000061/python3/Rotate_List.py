from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        nodes = list()
        node = head
        while node:
            nodes.append(node)
            node = node.next
        n = len(nodes)
        k %= n
        nodes[-1].next = nodes[0]
        nodes[-k - 1].next = None
        return nodes[-k]
