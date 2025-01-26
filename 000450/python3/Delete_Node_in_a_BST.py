from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None
            if node.val > key:
                l = dfs(node.left)
                node.left = l
            elif node.val < key:
                r = dfs(node.right)
                node.right = r
            else:
                if node.right is None and node.left is None:
                    return None
                elif node.right is None:
                    return node.left
                elif node.left is None:
                    return node.right
                else:
                    l = node.left
                    r = node.right
                    node = node.right
                    while r and r.left:
                        r = r.left
                    r.left = l
            return node
        
        return dfs(root)
