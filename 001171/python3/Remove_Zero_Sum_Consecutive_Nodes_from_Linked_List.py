from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = list()
        while head:
            if head.val != 0:
                vals.append(head.val)
            head = head.next
        stack = list()
        removed = True
        while removed:
            removed = False
            index = set()
            for i, val in enumerate(vals):
                for j, sum in enumerate(stack):
                    if sum + val == 0:
                        removed = True
                        for k in range(i, i - (len(stack) - j) - 1, -1):
                            index.add(k)
                        stack = list()
                        break
                    else:
                        stack[j] += val
                else:
                    stack.append(val)
            vals = [val for i, val in enumerate(vals) if i not in index]
            stack = list()

        # print(vals)
        prev = None
        while vals:
            val = vals.pop()
            curr = ListNode(val, prev)
            prev = curr
        return prev


l5 = ListNode(4)
l4 = ListNode(-3, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
s = Solution()
s.removeZeroSumSublists(l1)
