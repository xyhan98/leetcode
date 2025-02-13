from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        startNode = None
        
        def dfs(node: Optional[TreeNode]):
            if node.left:
                setattr(node.left, "parent", node)
                dfs(node.left)
            if node.right:
                setattr(node.right, "parent", node)
                dfs(node.right)
            if node.val == start:
                nonlocal startNode
                startNode = node
        
        setattr(root, "parent", None)
        dfs(root)

        infected = {start}
        i = -1
        queue = deque([startNode])
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for pointer in ["left", "right", "parent"]:
                    nxt = getattr(node, pointer)
                    if nxt and nxt.val not in infected:
                        infected.add(nxt.val)
                        queue.append(nxt)
            i += 1
        return i
