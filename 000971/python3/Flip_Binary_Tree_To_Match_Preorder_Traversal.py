from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        result = list()
        stack = list()
        i = 0
        node = root
        while i < len(voyage):
            while node:
                if node.val != voyage[i]:
                    return [-1]
                i += 1
                if node.left and node.right:
                    if node.left.val != voyage[i]:
                        node.left, node.right = node.right, node.left
                        result.append(node.val)
                stack.append(node)
                node = node.left
            while stack and not node:
                node = stack.pop()
                node = node.right
        return result
