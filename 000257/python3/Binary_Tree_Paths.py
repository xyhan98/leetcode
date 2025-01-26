from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = list()
        stack = list()

        def dfs(node: Optional[TreeNode]):
            stack.append(str(node.val))
            if node.left is None and node.right is None:
                s = "->".join(stack)
                result.append(s)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()

        dfs(root)
        return result
