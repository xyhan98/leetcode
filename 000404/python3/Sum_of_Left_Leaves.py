from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        setattr(root, "parent", None)

        def dfs(node: Optional[TreeNode]):
            if node.left is None and node.right is None:
                if node.parent and node == node.parent.left:
                    nonlocal result
                    result += node.val
                return
            if node.left:
                setattr(node.left, "parent", node)
                dfs(node.left)
            if node.right:
                setattr(node.right, "parent", node)
                dfs(node.right)
        
        dfs(root)
        return result
