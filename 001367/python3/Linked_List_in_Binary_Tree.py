from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        nodes = list()
        node = head
        while node:
            nodes.append(node.val)
            node = node.next
        
        stack = list()

        def dfs(node: TreeNode) -> bool:
            stack.append(node.val)
            if node.left is None and node.right is None:
                for i, val in enumerate(stack):
                    if val != nodes[0]:
                        continue
                    else:
                        if stack[i:i+len(nodes)] == nodes:
                            return True
            elif node.left is None:
                if dfs(node.right):
                    return True
            elif node.right is None:
                if dfs(node.left):
                    return True
            else:
                if dfs(node.left):
                    return True
                if dfs(node.right):
                    return True
            stack.pop()
            return False

        return dfs(root)


tn10 = TreeNode(3)
tn9 = TreeNode(1)
tn8 = TreeNode(8, tn9, tn10)
tn7 = TreeNode(6)
tn6 = TreeNode(1)
tn5 = TreeNode(2, tn7, tn8)
tn4 = TreeNode(2, tn6)
tn3 = TreeNode(4, tn5)
tn2 = TreeNode(4, None, tn4)
tn1 = TreeNode(1, tn2, tn3)

ln3 = ListNode(8)
ln2 = ListNode(2, ln3)
ln1 = ListNode(4, ln2)

s = Solution()
s.isSubPath(ln1, tn1)
