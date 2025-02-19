from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"
        result = list()
        queue = [root]
        while queue:
            vals = list()
            nxt = list()
            for node in queue:
                if node:
                    vals.append(str(node.val))
                    nxt.append(node.left)
                    nxt.append(node.right)
                else:
                    vals.append("#")
            result.append(",".join(vals))
            queue = nxt
        return ";".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        levels = data.split(";")
        if levels[0] == "#":
            return None
        levels = [level.split(",") for level in levels]
        root = TreeNode(int(levels[0][0]))
        queue = [root]
        i = 1
        while i < len(levels):
            nxt = list()
            for j, node in enumerate(queue):
                if levels[i][2 * j] != "#":
                    n = TreeNode(int(levels[i][2 * j]))
                    node.left = n
                    nxt.append(n)
                if levels[i][2 * j + 1] != "#":
                    n = TreeNode(int(levels[i][2 * j + 1]))
                    node.right = n
                    nxt.append(n)
            i += 1
            queue = nxt
        return root
