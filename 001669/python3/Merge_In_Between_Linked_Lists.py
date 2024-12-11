# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        i = 0
        while i < a - 1:
            head = head.next
            i += 1
        tail = head.next
        head.next = list2
        i += 1
        while i < b:
            tail = tail.next
            i += 1
        while head and head.next:
            head = head.next
        head.next = tail.next
        return list1
