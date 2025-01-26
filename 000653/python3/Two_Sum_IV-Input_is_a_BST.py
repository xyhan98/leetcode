from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            val = node.val
            if k - val in hashset:
                return True
            hashset.add(val)
            if dfs(node.left):
                return True
            return dfs(node.right)
        
        return dfs(root)
