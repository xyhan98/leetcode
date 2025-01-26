from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            lw, lwo = dfs(node.left)
            rw, rwo = dfs(node.right)
            return lwo + rwo + node.val, max(lw, lwo) + max(rw, rwo)
        
        return max(dfs(root))
