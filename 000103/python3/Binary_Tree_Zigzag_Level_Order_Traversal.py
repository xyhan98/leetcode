from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        if root is None:
            return result
        nodes = [root]
        while nodes:
            vals = list()
            queue = list()
            for node in nodes:
                vals.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if len(result) % 2 == 1:
                vals.reverse()
            result.append(vals)
            nodes = queue
        return result
