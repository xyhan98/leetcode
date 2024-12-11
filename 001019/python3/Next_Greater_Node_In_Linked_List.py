from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = list()
        stack = list()
        i = 0
        while head:
            val = 0
            while stack and stack[-1][1] < head.val:
                j, _ = stack.pop()
                result[j] = head.val
            stack.append((i, head.val))
            i += 1
            result.append(val)
            head = head.next
        return result
