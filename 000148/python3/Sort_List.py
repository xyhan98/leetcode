from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = dict()
        while head is not None:
            if head.val not in hashmap:
                hashmap[head.val] = list()
            hashmap[head.val].append(head)
            head = head.next
        dummy = ListNode()
        node = dummy
        vals = sorted(list(hashmap.keys()))
        for val in vals:
            for nxt in hashmap[val]:
                node.next = nxt
                node = node.next
        node.next = None
        return dummy.next
