from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start, end = None, None
        
        def dfs(node: Optional[TreeNode]):
            if node.left:
                setattr(node.left, "parent", node)
                dfs(node.left)
            if node.right:
                setattr(node.right, "parent", node)
                dfs(node.right)
            if node.val == startValue:
                nonlocal start
                start = node
            elif node.val == destValue:
                nonlocal end
                end = node
        
        setattr(root, "parent", None)
        dfs(root)

        stack = list()

        def dfs1(node: Optional[TreeNode], prev: Optional[TreeNode]) -> bool:
            if node.val == destValue:
                return True
            for direction in ["left", "right", "parent"]:
                nxt = getattr(node, direction)
                if nxt and nxt != prev:
                    if direction == "left":
                        stack.append("L")
                    elif direction == "right":
                        stack.append("R")
                    else:
                        stack.append("U")
                    if dfs1(nxt, node):
                        return True
                    stack.pop()
            return False
        
        dfs1(start, None)
        return "".join(stack)
