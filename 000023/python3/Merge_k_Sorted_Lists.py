import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l is not None]
        heapq.heapify(heap)
        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
            curr = curr.next
        return dummy.next
