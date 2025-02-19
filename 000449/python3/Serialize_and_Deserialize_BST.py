from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = list()

        def dfs(node: Optional[TreeNode]):
            if node is None:
                vals.append(str(-1))
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = [int(val) for val in data.split(",")]

        def dfs(lst: List[int]) -> Optional[TreeNode]:
            if not lst:
                return None
            val = lst[0]
            if val == -1:
                return None
            i = 1
            while i < len(lst):
                if lst[i] > val:
                    break
                i += 1
            node = TreeNode(val)
            node.left = dfs(lst[1:i])
            node.right = dfs(lst[i:])
            return node
        return dfs(vals)
