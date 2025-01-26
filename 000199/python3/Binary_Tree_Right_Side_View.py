from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result
        stack = [root]
        while stack:
            queue = list()
            for node in stack:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(stack[-1].val)
            stack = queue
        return result
