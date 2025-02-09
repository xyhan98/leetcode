from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        result = 0
        
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if node.left is None and node.right is None:
                return [1]
            ls, rs = list(), list()
            if node.left:
                ls = dfs(node.left)
            if node.right:
                rs = dfs(node.right)
            nonlocal result
            for l in ls:
                for r in rs:
                    if l + r <= distance:
                        result += 1
            return list(map(lambda x: x + 1, ls + rs))

        dfs(root)
        return result
