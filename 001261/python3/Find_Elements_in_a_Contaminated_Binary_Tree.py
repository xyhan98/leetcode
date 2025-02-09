from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.root = root
        queue = deque([self.root])
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    node.left.val = node.val * 2 + 1
                    queue.append(node.left)
                if node.right:
                    node.right.val = node.val * 2 + 2
                    queue.append(node.right)

    def find(self, target: int) -> bool:
        stack = [target]
        copy = target
        while copy > 0:
            if copy % 2 == 0:
                copy -= 2
            else:
                copy -= 1
            copy //= 2
            stack.append(copy)
        stack.reverse()
        node = self.root
        for i in range(1, len(stack)):
            if stack[i] % 2 == 0:
                if not node.right or node.right.val != stack[i]:
                    return False
                node = node.right
            else:
                if not node.left or node.left.val != stack[i]:
                    return False
                node = node.left
        return node.val == target
