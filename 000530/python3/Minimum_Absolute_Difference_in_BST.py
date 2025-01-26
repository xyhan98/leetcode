from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float('inf')

        def dfs(node: Optional[TreeNode], gt: int, lt: int):
            if node is None:
                return
            nonlocal result
            result = min(result, node.val - gt, lt - node.val)
            dfs(node.left, gt, node.val)
            dfs(node.right, node.val, lt)

        dfs(root, float('-inf'), float('inf'))
        return result
