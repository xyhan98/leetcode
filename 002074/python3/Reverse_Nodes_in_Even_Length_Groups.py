from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        groups = list()
        i = 1
        while head:
            group = list()
            for _ in range(i):
                group.append(head)
                head = head.next
                if not head:
                    break
            groups.append(group)
            i += 1
        
        def reverse(prev: Optional[ListNode], curr: ListNode, node: ListNode) -> ListNode:
            while prev != node:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        def dfs(i: int) -> Optional[ListNode]:
            if i == len(groups):
                return None
            node = dfs(i + 1)
            if len(groups[i]) % 2 == 1:
                groups[i][-1].next = node
                return groups[i][0]
            else:
                return reverse(node, groups[i][0], groups[i][-1])
        
        return dfs(0)
