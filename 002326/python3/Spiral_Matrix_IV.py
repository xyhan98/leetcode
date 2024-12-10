from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        round = min(m, n) // 2
        k = 0
        node = head
        while k < round:
            for j in range(0 + k, n - 1 - k):
                if node is None:
                    return matrix
                matrix[0 + k][j] = node.val
                node = node.next
            for i in range(0 + k, m - 1 - k):
                if node is None:
                    return matrix
                matrix[i][n - 1 - k] = node.val
                node = node.next
            for j in range(n - 1 - k, 0 + k, -1):
                if node is None:
                    return matrix
                matrix[m - 1 - k][j] = node.val
                node = node.next
            for i in range(m - 1 - k, 0 + k, -1):
                if node is None:
                    return matrix
                matrix[i][0 + k] = node.val
                node = node.next
            k += 1
        
        for i in range(k, m - k):
            for j in range(k, n - k):
                if node is None:
                    return matrix
                matrix[i][j] = node.val
                node = node.next
        return matrix
