from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = list()
        result = [0]

        def dfs(node: Optional[TreeNode]):
            stack.append(str(node.val))
            if node.left is None and node.right is None:
                s = "".join(stack)
                result[0] += int(s)
            elif node.left is None:
                dfs(node.right)
            elif node.right is None:
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        return result[0]
