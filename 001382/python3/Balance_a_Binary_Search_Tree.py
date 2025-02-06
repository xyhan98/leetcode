from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = list()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        def build(lst: List[TreeNode]) -> Optional[TreeNode]:
            if not lst:
                return None
            mid = (len(lst) - 1) // 2
            node = lst[mid]
            node.left = build(lst[:mid])
            node.right = build(lst[mid + 1:])
            return node
        
        dfs(root)
        return build(nodes)
