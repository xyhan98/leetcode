from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, left=root)
            return node
        i = 1
        queue = [root]
        while i < depth - 1:
            nxt = list()
            for node in queue:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            i += 1
        for node in queue:
            new = TreeNode(val, left=node.left)
            node.left = new
            new = TreeNode(val, right=node.right)
            node.right = new
        return root
        