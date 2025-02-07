from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            l = dfs(node.left, max(val, node.val))
            r = dfs(node.right, max(val, node.val))
            return l + r + int(node.val >= val)
        
        return dfs(root, root.val) if root else 0
