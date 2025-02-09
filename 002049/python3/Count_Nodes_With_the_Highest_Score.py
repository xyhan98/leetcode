from typing import List, Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        nodemap = {i: Node(val=i) for i in range(n)}
        for i in range(1, n):
            parent = nodemap[parents[i]]
            if parent.left is None:
                parent.left = nodemap[i]
            else:
                parent.right = nodemap[i]
        
        scoremap = dict()

        def dfs(node: Optional[Node]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            p = n - 1 - l - r
            product = max(l, 1) * max(r, 1) * max(p, 1)
            scoremap[product] = scoremap.get(product, 0) + 1
            return l + r + 1
        
        dfs(nodemap[0])
        score = max(scoremap.keys())
        return scoremap[score]
