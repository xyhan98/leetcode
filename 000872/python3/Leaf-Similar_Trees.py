from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], vals: List[int]):
            if node.left is None and node.right is None:
                vals.append(node.val)
                return
            if node.left:
                dfs(node.left, vals)
            if node.right:
                dfs(node.right, vals)

        leaves1 = list()
        dfs(root1, leaves1)
        leaves2 = list()
        dfs(root2, leaves2)
        return leaves1 == leaves2
