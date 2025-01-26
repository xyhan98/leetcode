from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        summap = dict()

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            if node.left:
                summap[l] = summap.get(l, 0) + 1
            r = dfs(node.right)
            if node.right:
                summap[r] = summap.get(r, 0) + 1
            return node.val + l + r
        
        val = dfs(root)
        summap[val] = summap.get(val, 0) + 1
        lst = [(v, k) for k, v in summap.items()]
        count = max(map(lambda x: x[0], lst))
        result = list()
        for v, k in lst:
            if v == count:
                result.append(k)
        return result
