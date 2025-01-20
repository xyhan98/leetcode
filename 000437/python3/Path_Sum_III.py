from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        stack = list()

        def dfs(node: Optional[TreeNode]):
            stack.append(node.val)
            total = sum(stack)
            for num in stack:
                if total == targetSum:
                    nonlocal result
                    result += 1
                total -= num
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()

        if not root:
            return result
        dfs(root)
        return result
