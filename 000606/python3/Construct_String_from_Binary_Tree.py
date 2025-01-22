from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""
            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return f"{node.val}({l})({r})"
            if not l and not r:
                return str(node.val)
            if l and not r:
                return f"{node.val}({l})"
            return f"{node.val}()({r})"
        
        return dfs(root)
