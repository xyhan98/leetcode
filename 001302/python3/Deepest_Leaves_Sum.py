from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = 0
        queue = [root]
        while queue:
            nxt = list()
            sum = 0
            for node in queue:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                sum += node.val
            queue = nxt
            result = sum
        return result
