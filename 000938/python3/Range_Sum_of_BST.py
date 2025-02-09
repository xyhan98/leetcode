from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            if low <= node.val <= high:
                nonlocal result
                result += node.val
        
        dfs(root)
        return result
