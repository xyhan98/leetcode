from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal result
            result = max(result, l, r)
            if node.left is None and node.right is None:
                return 0
            elif node.left is None:
                if node.val == node.right.val:
                    return r + 1
                return 0
            elif node.right is None:
                if node.val == node.left.val:
                    return l + 1
                return 0
            else:
                if node.left.val == node.right.val == node.val:
                    result = max(result, l + r + 2)
                    return max(l, r) + 1
                elif node.left.val == node.val:
                    return l + 1
                elif node.right.val == node.val:
                    return r + 1
                else:
                    return 0

        res = dfs(root)
        return max(res, result)
