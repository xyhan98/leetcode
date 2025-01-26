from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = list()
        queue = [root]
        while queue:
            nxt = list()
            val = 0
            for node in queue:
                val += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            val = round(val / len(queue), 5)
            result.append(val)
            queue = nxt
        return result
