from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            l, lh = dfs(node.left)
            if not l:
                return False, lh + 1
            r, rh = dfs(node.right)
            if not r:
                return False, rh + 1
            return abs(lh - rh) <= 1, max(lh, rh) + 1

        return dfs(root)[0]
        