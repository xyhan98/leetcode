from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = None
        result = float('-inf')
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if total:
                nonlocal result
                result = max(result, l * (total - l), r * (total - r))
            return l + r + node.val
        
        total = dfs(root)
        dfs(root)
        return result % (10**9 + 7)
