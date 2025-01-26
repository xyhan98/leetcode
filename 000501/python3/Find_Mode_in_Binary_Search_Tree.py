from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodemap = dict()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            nodemap[node.val] = nodemap.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        lst = [(v, k) for k, v in nodemap.items()]
        lst.sort(reverse=True)
        count = max(map(lambda x: x[0], lst))
        result = list()
        for v, k in lst:
            if v == count:
                result.append(k)
        return result
        