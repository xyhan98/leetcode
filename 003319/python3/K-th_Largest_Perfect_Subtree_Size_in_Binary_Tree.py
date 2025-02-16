from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        size_count_map = dict()
        
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            lb, lc = dfs(node.left)
            rb, rc = dfs(node.right)
            size = lc + rc + 1
            if lb and rb and lc == rc:
                size_count_map[size] = size_count_map.get(size, 0) + 1
                return True, size
            return False, size
        
        dfs(root)
        lst = [(size, c) for size, c in size_count_map.items()]
        lst.sort(reverse=True)
        count = 0
        for size, c in lst:
            count += c
            if count >= k:
                return size
        return -1
