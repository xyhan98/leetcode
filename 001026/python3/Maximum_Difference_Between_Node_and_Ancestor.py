from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return float('inf'), float('-inf')
            lmin, lmax = dfs(node.left)
            rmin, rmax = dfs(node.right)
            nonlocal result
            if lmin != float('inf'):
                result = max(result, abs(node.val - lmin))
            if lmax != float('-inf'):
                result = max(result, abs(node.val - lmax))
            if rmin != float('inf'):
                result = max(result, abs(node.val - rmin))
            if rmax != float('-inf'):
                result = max(result, abs(node.val - rmax))
            return min(lmin, rmin, node.val), max(lmax, rmax, node.val)
        
        dfs(root)
        return result
        