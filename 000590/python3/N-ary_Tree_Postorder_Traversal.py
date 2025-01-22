from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = list()

        def dfs(node: Optional[Node]):
            if node is None:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result
