class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        cache[-1] = 1
        cache[-2] = 1
        for i in range(len(cache) - 3, -1, -1):
            cache[i] += cache[i + 1] + cache[i + 2]
        return cache[0]
