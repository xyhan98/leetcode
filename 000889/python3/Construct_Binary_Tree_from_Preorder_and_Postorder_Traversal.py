from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        node = TreeNode(preorder[0])
        preorder = preorder[1:]
        postorder = postorder[:-1]
        val = preorder[0]
        i = postorder.index(val)
        node.left = self.constructFromPrePost(preorder[:i + 1], postorder[:i + 1])
        node.right = self.constructFromPrePost(preorder[i + 1:], postorder[i + 1:])
        return node
