from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        val = max(nums)
        i = nums.index(val)
        l = self.constructMaximumBinaryTree(nums[:i])
        r = self.constructMaximumBinaryTree(nums[i + 1:])
        return TreeNode(val, left=l, right=r)
