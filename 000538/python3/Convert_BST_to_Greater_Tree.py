from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return val
            val = dfs(node.right, val)
            node.val += val
            return dfs(node.left, node.val)
        
        dfs(root, 0)
        return root
