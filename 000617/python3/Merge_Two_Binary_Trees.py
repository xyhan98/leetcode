from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            l = self.mergeTrees(root1.left, root2.left)
            r = self.mergeTrees(root1.right, root2.right)
            node = TreeNode(root1.val + root2.val, left=l, right=r)
            return node
            