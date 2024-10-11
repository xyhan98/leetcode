from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while head:
            if head and head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
            else:
                node.next = head
                node = node.next
            head = head.next
        node.next = None
        return dummy.next
            