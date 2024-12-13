from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        if max(matchsticks) > length:
            return False
        matchsticks.sort(reverse=True)
        sticks = dict()
        for stick in matchsticks:
            sticks[stick] = sticks.get(stick, 0) + 1
        
        def dfs(sum: int, n: int, val: int) -> bool:
            if n == 4:
                return True
            if n > 4:
                return False
            for stick, count in sticks.items():
                if count == 0 or stick > val:
                    continue
                sticks[stick] -= 1
                if sum + stick < length:
                    if dfs(sum + stick, n, stick):
                        return True
                elif sum + stick == length:
                    if dfs(0, n + 1, matchsticks[0]):
                        return True
                sticks[stick] += 1
            return False

        return dfs(0, 0, matchsticks[0])
