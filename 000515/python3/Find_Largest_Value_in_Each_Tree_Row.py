from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result
        queue = [root]
        while queue:
            nxt = list()
            val = queue[0].val
            for node in queue:
                val = max(val, node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            result.append(val)
        return result
