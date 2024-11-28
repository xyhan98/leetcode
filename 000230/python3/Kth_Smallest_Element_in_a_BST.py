from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = list()
        node = root
        i, val = 0, 0
        while i < k:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            i += 1
            val = node.val
            node = node.right
        return val
