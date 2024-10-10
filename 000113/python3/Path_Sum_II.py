from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = list()
        stack = list()

        def dfs(node: Optional[TreeNode], sum: int):
            if node is None:
                return
            stack.append(node.val)
            sum -= node.val
            if sum == 0 and node.left is None and node.right is None:
                result.append(list(stack))
            else:
                dfs(node.left, sum)
                dfs(node.right, sum)
            stack.pop()
        
        dfs(root, targetSum)
        return result
