from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            lsum, lcount = dfs(node.left)
            rsum, rcount = dfs(node.right)
            sum = lsum + rsum + node.val
            count = lcount + rcount + 1
            if sum // count == node.val:
                nonlocal result
                result += 1
            return sum, count

        dfs(root)
        return result
