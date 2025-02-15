from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        queue = [root]
        while queue:
            nxt = list()
            vals = list()
            total = 0
            for node in queue:
                t = 0
                if node.left:
                    nxt.append(node.left)
                    t += node.left.val
                if node.right:
                    nxt.append(node.right)
                    t += node.right.val
                vals.append(t)
                total += t
            for i, node in enumerate(queue):
                val = total - vals[i]
                if node.left:
                    node.left.val = val
                if node.right:
                    node.right.val = val
            queue = nxt
        
        return root
