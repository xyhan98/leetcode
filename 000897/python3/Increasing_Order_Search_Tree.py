from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], right: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return right
            node.right = dfs(node.right, right)
            left = node.left
            node.left = None
            return dfs(left, node)
        
        return dfs(root, None)
