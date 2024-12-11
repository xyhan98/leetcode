from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(node: Optional[Node], nxt: Optional[Node]) -> Node:
            if node is None:
                return nxt
            nxt = dfs(node.next, nxt)
            if node.child:
                nxt = dfs(node.child, nxt)
                node.child = None
            node.next = nxt
            if nxt is not None:
                nxt.prev = node
            return node
        
        return dfs(head, None)
