from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if node1 is None:
                return None
            if node1 == target:
                return node2
            node = dfs(node1.left, node2.left)
            if node:
                return node
            node = dfs(node1.right, node2.right)
            return node
        
        return dfs(original, cloned)
