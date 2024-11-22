from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = list()
        node = root
        while node:
            if node.left is None and node.right is None:
                if stack:
                    node.right = stack.pop()
            elif node.left is None and node.right:
                pass
            elif node.left and node.right is None:
                node.right = node.left
                node.left = None
            else:
                stack.append(node.right)
                node.right = node.left
                node.left = None
            node = node.right
