from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        i = 0
        while node:
            i += 1
            node = node.next
        num = i // k
        n = i % k
        result = list()
        j = 0
        while j < k:
            result.append(head)
            m = num - 1 + (1 if n > 0 else 0)
            for _ in range(0, m):
                head = head.next
                if not head:
                    break
            else:
                if head:
                    nxt = head.next
                    head.next = None
                    head = nxt
            j += 1
            n -= 1
        return result
