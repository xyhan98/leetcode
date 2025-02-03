from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if node.left is None and node.right is None:
                if val + node.val < limit:
                    return None
                return node
            if node.left:
                node.left = dfs(node.left, val + node.val)
            if node.right:
                node.right = dfs(node.right, val + node.val)
            if node.left is None and node.right is None:
                return None
            return node

        return dfs(root, 0)

t5 = TreeNode(4)
t4 = TreeNode(-5)
t3 = TreeNode(-3, left=t5)
t2 = TreeNode(2, left=t4)
t1 = TreeNode(1, left=t2, right=t3)
s = Solution()
s.sufficientSubset(t1, -1)
