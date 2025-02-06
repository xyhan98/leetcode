from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodemap = {i: Node(val=i) for i in range(n)}
        for i, (left, right) in enumerate(zip(leftChild, rightChild)):
            # print(i, left, right)
            node = nodemap[i]
            if left != -1:
                node.left = nodemap[left]
                if nodemap[left].parent:
                    return False
                nodemap[left].parent = node
            if right != -1:
                node.right = nodemap[right]
                if nodemap[right].parent:
                    return False
                nodemap[right].parent = node
        
        visit = set()
        root = None
        for i, node in nodemap.items():
            if node.parent is None:
                root = node
                break
        
        def dfs(node: Node) -> bool:
            if node.val in visit:
                return False
            visit.add(node.val)
            if node.left:
                if not dfs(node.left):
                    return False
            if node.right:
                if not dfs(node.right):
                    return False
            return True
        
        if root is None:
            return False
        b = dfs(root)
        return len(visit) == n if b else b
