from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = list()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        
        dfs(root)
        result = list()

        for target in queries:
            i, j = 0, len(vals) - 1
            while i <= j:
                mid = (i + j) // 2
                if vals[mid] == target:
                    result.append([target, target])
                    break
                elif vals[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if j == -1:
                    result.append([-1, vals[0]])
                elif i == len(vals):
                    result.append([vals[-1], -1])
                else:
                    result.append([vals[j], vals[i]])
        return result
