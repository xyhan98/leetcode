from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = list()
        if not root:
            return result
        queue = [root]
        while queue:
            nxt = list()
            vals = list()
            for node in queue:
                vals.append(node.val)
                for child in node.children:
                    if child:
                        nxt.append(child)
            result.append(vals)
            queue = nxt
        return result
