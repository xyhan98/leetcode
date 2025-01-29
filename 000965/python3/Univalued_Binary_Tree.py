from typing import Optional, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], vals: Set[int]):
            if node is None:
                return
            vals.add(node.val)
            dfs(node.left, vals)
            dfs(node.right, vals)
        
        vals = set()
        dfs(root, vals)
        return len(vals) == 1
