from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = list()
        
        def convert() -> int:
            res = 0
            for val in stack:
                res *= 2
                res += val
            return res

        def dfs(node: Optional[TreeNode]):
            stack.append(node.val)
            if node.left is None and node.right is None:
                num = convert()
                nonlocal result
                result += num
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        return result
