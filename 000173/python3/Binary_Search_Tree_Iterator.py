from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = root
        self.stack = list()

    def next(self) -> int:
        node = self.pointer
        while node:
            self.stack.append(node)
            node = node.left
        node = self.stack.pop()
        self.pointer = node.right
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.pointer is not None
