class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        vals = preorder.split(",")
        if vals[-1] != "#":
            return False
        vals = vals[:-1]
        stack = list()
        i = 0
        while i < len(vals):
            j = 0
            while i + j < len(vals) and vals[i + j] != "#":
                node = TreeNode(vals[i + j])
                stack.append(node)
                j += 1
            while i + j <len(vals) and vals[i + j] == "#":
                if not stack:
                    return False
                node = stack.pop()
                j += 1
            i += j
        return not stack
