from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        l = self.pruneTree(root.left)
        r = self.pruneTree(root.right)
        if not l and not r and root.val != 1:
            return None
        root.left = l
        root.right = r
        return root
