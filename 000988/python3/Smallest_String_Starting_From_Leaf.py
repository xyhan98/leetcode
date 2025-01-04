from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = list()
        stack = list()

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            stack.append(node.val)
            if node.left is None and node.right is None:
                temp = list(stack)
                temp.reverse()
                paths.append(temp)
            elif node.left is None:
                dfs(node.right)
            elif node.right is None:
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
            stack.pop()
        
        dfs(root)
        # print(paths)
        paths.sort()
        path = paths[0]
        return "".join(map(lambda x: chr(x + 97), path))
