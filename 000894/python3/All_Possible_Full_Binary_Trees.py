from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        result = list()
        if n % 2 == 0:
            return result
        cache = dict()
        cache[1] = [TreeNode(0)]

        def dfs(num: int) -> List[Optional[TreeNode]]:
            if num in cache:
                return cache[num]
            res = list()
            for i in range(1, num, 2):
                ls = dfs(i)
                rs = dfs(num - i - 1)
                for l in ls:
                    for r in rs:
                        node = TreeNode(0, left=l, right=r)
                        res.append(node)
            cache[num] = res
            return cache[num]
        
        return dfs(n)
