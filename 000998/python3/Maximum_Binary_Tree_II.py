from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val < val:
            node = TreeNode(val=val, left=root)
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
