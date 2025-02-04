from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        left = 0
        right = 0
        parent = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                nonlocal left, right
                left = l
                right = r
            return l + r + 1

        dfs(root)
        parent = n - 1 - left - right
        if parent > n - parent or left > n - left or right > n - right:
            return True
        return False
