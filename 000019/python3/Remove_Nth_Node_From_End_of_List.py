from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def dfs(node: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
            if node is None:
                return None, 0
            nxt, i = dfs(node.next)
            i += 1
            if i == n:
                node.next = None
                return nxt, i
            else:
                node.next = nxt
                return node, i
        
        return dfs(head)[0]
