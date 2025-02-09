from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            nxt = list()
            indices = list()
            for i, node in enumerate(queue):
                if node:
                    nxt.append(node.left)
                    nxt.append(node.right)
                else:
                    indices.append(i)
            s = set(nxt)
            if indices:
                if len(set(queue[indices[0]:])) > 1:
                    return False
                elif len(s) > 1:
                    return False
            if len(s) == 1 and None in s:
                break
            queue = nxt
        return True
