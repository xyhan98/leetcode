from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = dict()
        result = list()

        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""
            l = dfs(node.left)
            r = dfs(node.right)
            if not l and not r:
                s = f"{node.val}"
            elif l and not r:
                s = f"{node.val}({l})"
            elif not l and r:
                s = f"{node.val}()({r})"
            else:
                s = f"{node.val}({l})({r})"
            hashmap[s] = hashmap.get(s, 0) + 1
            if hashmap[s] == 2:
                result.append(node)
            return s
        
        dfs(root)
        return result
