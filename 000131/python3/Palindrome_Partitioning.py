from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = list()
        stack = list()

        def isPalindrome(t: str) -> bool:
            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i: int):
            if i == len(s):
                result.append(list(stack))
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    stack.append(s[i:j + 1])
                    dfs(j + 1)
                    stack.pop()
        
        dfs(0)
        return result
