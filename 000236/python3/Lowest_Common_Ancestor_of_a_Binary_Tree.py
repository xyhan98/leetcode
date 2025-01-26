# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            if (l and r) or (node.val in {p.val, q.val} and (l or r)):
                nonlocal result
                result = node
                return True
            return node.val in {p.val, q.val} or l or r
            
        dfs(root)
        return result
