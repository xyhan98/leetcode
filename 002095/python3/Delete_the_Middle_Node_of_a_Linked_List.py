from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast is None:
            prev.next = prev.next.next if prev.next else None
        else:
            slow.next = slow.next.next if slow.next else None
        return dummy.next
