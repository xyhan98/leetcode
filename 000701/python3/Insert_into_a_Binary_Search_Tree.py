from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val < val:
            node = self.insertIntoBST(root.right, val)
            root.right = node
        else:
            node = self.insertIntoBST(root.left, val)
            root.left = node
        return root
