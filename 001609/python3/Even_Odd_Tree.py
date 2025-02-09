from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        i = 0
        while queue:
            vals = list()
            nxt = list()
            for node in queue:
                vals.append(node.val)
                if i % 2 == 0:
                    if vals[-1] % 2 != 1:
                        return False
                    if len(vals) > 1:
                        if vals[-2] >= vals[-1]:
                            return False
                else:
                    if vals[-1] % 2 != 0:
                        return False
                    if len(vals) > 1:
                        if vals[-2] <= vals[-1]:
                            return False
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            i += 1
        return True
