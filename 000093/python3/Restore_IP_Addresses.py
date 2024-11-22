from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = list()
        if not 4 <= len(s) <= 12:
            return result
        stack = list()

        def dfs(i: int):
            if i == len(s) and len(stack) == 4:
                result.append(".".join(stack))
                return
            if i >= len(s) or len(stack) >= 4:
                return
            for j in range(1, min(4, len(s) - i + 1)):
                if s[i] == "0" and j > 1:
                    break
                c = s[i:i+j]
                if int(c) > 255:
                    break
                stack.append(c)
                dfs(i + j)
                stack.pop()
        
        dfs(0)
        return result
