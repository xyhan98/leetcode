from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node: Optional[TreeNode], vals: List[int], recover=False):
            if node is None:
                return
            dfs(node.left, vals, recover)
            if not recover:
                vals.append(node.val)
            else:
                node.val = vals.pop()
            dfs(node.right, vals, recover)
        
        vals = list()
        dfs(root, vals)
        vals.sort()
        vals.reverse()
        dfs(root, vals, True)
