from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Memory Limit Exceeded
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        queue = [root]
        while queue:
            nxt = [None] * 2 * len(queue)

            i, j = 0, len(queue) - 1
            while i < len(queue) and queue[i] is None:
                i += 1
            if i != len(queue):
                while j >= 0 and queue[j] is None:
                    j -= 1
                result = max(result, j - i + 1)
            
            for i, node in enumerate(queue):
                if node:
                    nxt[i * 2] = node.left
                    nxt[i * 2 + 1] = node.right
            
            if len(set(nxt)) == 1 and None == nxt[0]:
                break
            queue = nxt

        return result
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        setattr(root, "index", 0)
        queue = [root]
        while queue:
            nxt = list()
            result = max(result, queue[-1].index - queue[0].index + 1)
            for node in queue:
                if node.left:
                    setattr(node.left, "index", node.index * 2)
                    nxt.append(node.left)
                if node.right:
                    setattr(node.right, "index", node.index * 2 + 1)
                    nxt.append(node.right)
            queue = nxt
        
        return result
