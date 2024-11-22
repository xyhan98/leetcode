from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(nodes: List[Optional[TreeNode]]) -> List[List[int]]:
            if not nodes:
                return []
            vals = list()
            children = list()
            for node in nodes:
                vals.append(node.val)
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            result = dfs(children)
            result.append(vals)
            return result

        return dfs([root]) if root else []
