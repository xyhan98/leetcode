from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cache = dict()
        
        def dfs(i: int, total: int) -> List[int]:
            if 2 * i < n:
                l = dfs(2 * i, total + cost[i - 1])
                r = dfs(2 * i + 1, total + cost[i - 1])
                res = l + r
            else:
                res = [total + cost[i - 1]]
            cache[i] = res
            return res
        
        dfs(1, 0)
        # print(cache)
        result = 0
        maxSum = max(cache[1])

        def dfs1(i: int):
            total = cache[i]
            nonlocal result
            if 2 * i < n:
                mid = len(total) // 2
                l = total[:mid]
                r = total[mid:]
                lmax, rmax = max(l), max(r)
                if lmax == maxSum:
                    increment = maxSum - rmax
                    result += increment
                    r = [val + increment for val in r]
                else:
                    increment = maxSum - lmax
                    result += increment
                    l = [val + increment for val in l]
                cache[2 * i] = l
                cache[2 * i + 1] = r
                dfs1(2 * i)
                dfs1(2 * i + 1)
            else:
                result += total[0] - maxSum
        
        dfs1(1)
        return result
