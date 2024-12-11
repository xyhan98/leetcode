from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        def dfs(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return node
            nxt = dfs(node.next)
            if node.val in nums:
                return nxt
            else:
                node.next = nxt
                return node
        
        return dfs(head)
