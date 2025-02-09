from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        paths = list()
        stack = list()
        
        def dfs(node: Optional[TreeNode]):
            stack.append(node.val)
            if node.left is None and node.right is None:
                paths.append(list(stack))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        length = max(map(len, paths))
        paths = list(filter(lambda x: len(x) == length, paths))
        if len(paths) > 1:
            for i in range(length):
                if len(set(map(lambda x: x[i], paths))) != 1:
                    paths = [paths[0][:i]]
                    break
        i = 1
        node = root
        while i < len(paths[0]):
            if node.left and node.left.val == paths[0][i]:
                node = node.left
            else:
                node = node.right
            i += 1
        return node
