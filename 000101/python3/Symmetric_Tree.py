from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None or p.val != q.val:
                return False
            return False if not dfs(p.left, q.right) else dfs(p.right, q.left)
        
        return dfs(root.left, root.right)
