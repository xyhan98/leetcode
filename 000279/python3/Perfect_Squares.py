class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n for _ in range(n + 1)]
        cache[0] = 0
        for i in range(1, int(n**0.5) + 1):
            v = i**2
            for j in range(1, n + 1):
                if j < v:
                    continue
                cache[j] = min(cache[j], cache[j - v] + 1)
            # print(cache)
        return cache[-1]
