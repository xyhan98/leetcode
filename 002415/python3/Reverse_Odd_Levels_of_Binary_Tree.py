from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        i = 0
        prev = list()
        curr = [root]
        while curr:
            nxt = list()
            for node in curr:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if i % 2 == 1:
                curr.reverse()
            for j, node in enumerate(prev):
                node.left = curr[2 * j]
                node.right = curr[2 * j + 1]
            prev = curr
            curr = nxt
            i += 1
        return root
