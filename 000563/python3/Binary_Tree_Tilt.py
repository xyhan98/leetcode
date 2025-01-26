from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            val = node.val
            node.val = abs(l - r)
            return val + l + r
        
        dfs(root)
        stack = list()
        result = 0
        node = root
        while node:
            while node:
                stack.append(node)
                node = node.left
            while stack and node is None:
                node = stack.pop()
                result += node.val
                node = node.right
        
        return result
