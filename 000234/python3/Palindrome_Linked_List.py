from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        n1, n2 = head, prev
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        return True
