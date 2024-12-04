from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        while head:
            if head.val in nums:
                while head and head.val in nums:
                    nums.remove(head.val)
                    head = head.next
                result += 1
            else:
                head = head.next
        return result
