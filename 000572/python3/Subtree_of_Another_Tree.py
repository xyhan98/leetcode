from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None or n1.val != n2.val:
                return False
            else:
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
        
        if root is None and subRoot is None:
            return True
        elif subRoot is None:
            return True
        elif root is None:
            return False
        else:
            if root.val == subRoot.val:
                if dfs(root, subRoot):
                    return True
            if self.isSubtree(root.left, subRoot):
                return True
            if self.isSubtree(root.right, subRoot):
                return True
            return False
