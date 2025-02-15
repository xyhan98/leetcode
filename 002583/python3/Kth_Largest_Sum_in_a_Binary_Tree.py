from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]
        sum_count_map = dict()
        while queue:
            nxt = list()
            total = 0
            for node in queue:
                total += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            sum_count_map[total] = sum_count_map.get(total, 0) + 1
        lst = [(sum, c) for sum, c in sum_count_map.items()]
        lst.sort(reverse=True)
        count = 0
        for sum, c in lst:
            count += c
            if count >= k:
                return sum
        return -1
