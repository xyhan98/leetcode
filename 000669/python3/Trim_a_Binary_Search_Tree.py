from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        l = self.trimBST(root.left, low, high)
        r = self.trimBST(root.right, low, high)
        root.left = l
        root.right = r
        if root.val < low:
            return r
        elif root.val > high:
            return l
        else:
            return root
