from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            if node.left:
                setattr(node.left, "parent", node)
            if node.right:
                setattr(node.right, "parent", node)
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal result
            result = max(result, l, r)
            if node.parent:
                if node.parent.left == node:
                    return r + 1
                elif node.parent.right == node:
                    return l + 1
            return max(l, r)
        
        setattr(root, "parent", None)
        res = dfs(root)
        return max(result, res)
