from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = list()
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(num):
                if len(stack) >= 3:
                    result.extend(stack)
                    return True
                return False
            for j in range(1, len(num) + 1 - i):
                s = num[i:i + j]
                if len(s) > 1 and s[0] == "0":
                    break
                if int(s) >= 2**31:
                    break
                stack.append(int(s))
                if (len(stack) >= 3 and stack[-1] == stack[-2] + stack[-3]) or len(stack) < 3:
                    if dfs(i + j):
                        return True
                elif len(stack) >= 3 and stack[-1] > stack[-2] + stack[-3]:
                    stack.pop()
                    break
                stack.pop()
            return False

        dfs(0)
        return result

s = Solution()
s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")
