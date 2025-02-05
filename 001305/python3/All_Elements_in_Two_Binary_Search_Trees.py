from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def dfs(node: Optional[TreeNode], vals: List[int]):
            if node is None:
                return
            dfs(node.left, vals)
            vals.append(node.val)
            dfs(node.right, vals)
        
        vals1, vals2 = list(), list()
        dfs(root1, vals1)
        dfs(root2, vals2)

        result = list()
        i, j = 0, 0
        while i < len(vals1) and j < len(vals2):
            if vals1[i] <= vals2[j]:
                result.append(vals1[i])
                i += 1
            else:
                result.append(vals2[j])
                j += 1
        if i < len(vals1):
            result.extend(vals1[i:])
        elif j < len(vals2):
            result.extend(vals2[j:])
        
        return result
