from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], l: float, r: float) -> bool:
            if node is None:
                return True
            if not l < node.val < r:
                return False
            return False if not dfs(node.left, l, node.val) else dfs(node.right, node.val, r)
        
        return dfs(root, float('-inf'), float('inf'))
