from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodemap = {c: TreeNode(val=c) for _, c, _ in descriptions}
        root = None
        for p, c, b in descriptions:
            if p not in nodemap:
                root = TreeNode(val=p)
                nodemap[p] = root
            if b:
                nodemap[p].left = nodemap[c]
            else:
                nodemap[p].right = nodemap[c]
        return root
