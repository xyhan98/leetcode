from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        while queue:
            nodes = deque(list())
            nxt = None
            for i in range(len(queue) - 1, -1, -1):
                node = queue[i]
                node.next = nxt
                nxt = node
                if node.right:
                    nodes.appendleft(node.right)
                if node.left:
                    nodes.appendleft(node.left)
            queue = nodes
        return root
