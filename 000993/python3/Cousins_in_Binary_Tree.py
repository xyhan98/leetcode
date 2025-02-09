from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        paths = list()
        stack = list()

        def dfs(node: Optional[TreeNode]):
            stack.append(node.val)
            if node.val in {x, y}:
                paths.append(list(stack))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        return len(paths[0]) == len(paths[1]) and paths[0][-2] != paths[1][-2]
