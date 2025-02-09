from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        hashmap = dict()
        result = 0

        def dfs(node: Optional[TreeNode]):
            hashmap[node.val] = hashmap.get(node.val, 0) + 1
            if node.left is None and node.right is None:
                nonlocal result
                result += int(len([v for k, v in hashmap.items() if v % 2 == 1]) <= 1)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            hashmap[node.val] -= 1
        
        dfs(root)
        return result
