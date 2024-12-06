from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        nodes = list()
        node = head
        while node:
            nodes.append(node)
            node = node.next
        if k > len(nodes) // 2:
            k = len(nodes) - k + 1
        nodes[k - 1], nodes[-k] = nodes[-k], nodes[k - 1]

        nodes[k - 1].next = nodes[k]
        nodes[-k].next = nodes[-(k - 1)] if k > 1 else None
        if k > 1:
            nodes[k - 2].next = nodes[k - 1]
        if len(nodes) > k + 1:
            nodes[-(k + 1)].next = nodes[-k]
            
        return nodes[0]

l5 = ListNode(64)
l4 = ListNode(35, l5)
l3 = ListNode(66, l4)
l2 = ListNode(46, l3)
l1 = ListNode(80, l2)
s = Solution()
l = s.swapNodes(l1, 1)
