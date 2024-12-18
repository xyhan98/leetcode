class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0 for _ in range(len(s) + 1)]
        cache[-1] = 1
        cache[-2] = 1 if s[-1] != "0" else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                continue
            code = s[i:i+2]
            if int(code) <= 26:
                cache[i] = cache[i + 1] + cache[i + 2]
            else:
                cache[i] = cache[i + 1]
        return cache[0]
