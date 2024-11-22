# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        indexNodeMap = dict()

        def dfs(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            curr = Node(node.val)
            indexNodeMap[node] = curr
            curr.next = dfs(node.next)
            curr.random = indexNodeMap.get(node.random, None)
            return curr

        return dfs(head)
