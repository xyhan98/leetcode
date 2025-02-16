from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        result = 0
        while queue:
            nxt = list()
            vals = list()
            for node in queue:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            # for i in range(len(vals) - 1):
            #     k = i
            #     for j in range(i + 1, len(vals)):
            #         if vals[k] > vals[j]:
            #             k = j
            #     if k != i:
            #         result += 1
            #         vals[i], vals[k] = vals[k], vals[i]

            val_index_map = {val: i for i, val in enumerate(vals)}
            sorted_vals = sorted(vals)
            for i, val in enumerate(vals):
                if val != sorted_vals[i]:
                    result += 1
                    j = val_index_map[sorted_vals[i]]
                    vals[i], vals[j] = vals[j], vals[i]
                    val_index_map[sorted_vals[i]] = i
                    val_index_map[val] = j
        return result
