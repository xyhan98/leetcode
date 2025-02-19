from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return val
            r = dfs(node.right, val)
            val = r + node.val
            node.val = val
            return dfs(node.left, val)
        
        dfs(root, 0)
        return root
