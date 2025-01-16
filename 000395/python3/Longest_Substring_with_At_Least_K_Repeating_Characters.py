class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        result = 0
        if not s:
            return result
        hashmap = dict()
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        if all(map(lambda x: x >= k, hashmap.values())):
            return len(s)

        prev = -1
        for i, c in enumerate(s):
            if hashmap[c] < k:
                res = self.longestSubstring(s[prev + 1:i], k)
                result = max(result, res)
                prev = i
        res = self.longestSubstring(s[prev + 1:], k)
        result = max(result, res)
        return result

s = Solution()
s.longestSubstring("bbaaacbd", 3)
