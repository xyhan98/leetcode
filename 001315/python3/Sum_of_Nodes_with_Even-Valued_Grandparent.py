from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = list()

        def dfs(node: Optional[TreeNode]):
            stack.append(node.val)
            if len(stack) > 2 and stack[-3] % 2 == 0:
                nonlocal result
                result += node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        return result
