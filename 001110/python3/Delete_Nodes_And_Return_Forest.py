from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = list()
        to_delete = set(to_delete)

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val in to_delete:
                if l:
                    result.append(l)
                if r:
                    result.append(r)
                return None
            node.left = l
            node.right = r
            return node

        node = dfs(root)
        if node:
            result.append(node)
        return result
