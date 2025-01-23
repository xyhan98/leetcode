from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1
        
        height = dfs(root) - 1
        m, n = height + 1, 2**(height + 1) - 1
        result = [["" for _ in range(n)] for _ in range(m)]

        result[0][(n - 1) // 2] = f"{root.val}"
        queue = deque()
        queue.append((root, 0, (n - 1) // 2))

        while queue:
            n = len(queue)
            for _ in range(n):
                node, i, j = queue.popleft()
                if node.left:
                    r, c = i + 1, j - 2**(height - i - 1)
                    result[r][c] = f"{node.left.val}"
                    queue.append((node.left, r, c))
                if node.right:
                    r, c = i + 1, j + 2**(height - i - 1)
                    result[r][c] = f"{node.right.val}"
                    queue.append((node.right, r, c))

        return result
