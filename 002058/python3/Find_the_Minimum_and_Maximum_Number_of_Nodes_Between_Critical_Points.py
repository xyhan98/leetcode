from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        stack = list()
        prev, curr = head, head.next
        i = 1
        minD = float('inf')
        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if len(stack) < 2:
                    stack.append(i)
                    if len(stack) == 2:
                        minD = min(minD, stack[1] - stack[0])
                else:
                    minD = min(minD, i - stack[-1])
                    stack[-1] = i
            i += 1
            prev, curr = curr, nxt
        return [minD, stack[1] - stack[0]] if len(stack) == 2 else [-1, -1]
