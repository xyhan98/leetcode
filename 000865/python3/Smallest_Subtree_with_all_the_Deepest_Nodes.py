from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            h = max(lh, rh) + 1
            setattr(node, "height", h)
            return h
        
        dfs(root)
        node = root
        while node:
            if not node.left and not node.right:
                break
            elif node.left and node.right:
                if node.left.height == node.right.height:
                    break
                elif node.left.height > node.right.height:
                    node = node.left
                else:
                    node = node.right
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
        return node
