from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            if node.left:
                setattr(node.left, "parent", node)
                dfs(node.left)
            if node.right:
                setattr(node.right, "parent", node)
                dfs(node.right)
        
        dfs(root)
        setattr(root, "parent", None)

        result = list()
        # edge case
        if k == 0:
            result.append(target.val)
            return result

        def dfs1(node: Optional[TreeNode], i: int):
            if node is None or i > k:
                return
            if i == k:
                result.append(node.val)
                return
            dfs1(node.left, i + 1)
            dfs1(node.right, i + 1)
        
        dfs1(target.left, 1)
        dfs1(target.right, 1)

        i = 0
        copy = target
        while i < k and copy.parent:
            nxt = copy.parent
            i += 1
            if i == k:
                result.append(nxt.val)
            else:
                if nxt.left and nxt.left != copy:
                    dfs1(nxt.left, i + 1)
                if nxt.right and nxt.right != copy:
                    dfs1(nxt.right, i + 1)
                copy = nxt
        return result
