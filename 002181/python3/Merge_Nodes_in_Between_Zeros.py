from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node: Optional[ListNode]) -> tuple[ListNode, int]:
            if node and node.val == 0 and node.next is None:
                return None, 0
            nxt, val = dfs(node.next)
            if node.val == 0:
                nxt = ListNode(val, nxt)
                val = 0
            else:
                val += node.val
            return nxt, val
        
        return dfs(head)[0]
