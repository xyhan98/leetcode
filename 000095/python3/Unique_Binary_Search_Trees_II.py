from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def dfs(nums: List[int]) -> List[Optional[TreeNode]]:
            if not nums:
                return [None]
            result = list()
            for i, num in enumerate(nums):
                ls = dfs(nums[:i])
                rs = dfs(nums[i+1:])
                for l in ls:
                    for r in rs:
                        node = TreeNode(val=num, left=l, right=r)
                        result.append(node)
            return result
        
        return dfs([i for i in range(1, n + 1)])
