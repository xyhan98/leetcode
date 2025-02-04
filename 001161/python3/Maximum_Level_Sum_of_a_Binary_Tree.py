from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        level = 0
        queue = deque([root])
        i = 1
        while queue:
            length = len(queue)
            sum = 0
            for _ in range(length):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum > result:
                result = sum
                level = i
            i += 1
        return level
