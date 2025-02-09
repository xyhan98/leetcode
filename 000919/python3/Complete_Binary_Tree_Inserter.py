from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.vals = dict()
        queue = [root]
        while queue:
            nxt = list()
            for node in queue:
                self.vals[len(self.vals)] = node
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        self.vals[len(self.vals)] = node
        n = len(self.vals) - 1
        if n % 2 == 0:
            parent = self.vals[(n - 2) // 2]
            parent.right = node
        else:
            parent = self.vals[(n - 1) // 2]
            parent.left = node
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
