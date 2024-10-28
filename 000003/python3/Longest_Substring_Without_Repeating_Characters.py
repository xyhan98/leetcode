class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hashmap = dict()
        prev = 0
        for i, c in enumerate(s):
            result = max(result, len(hashmap))
            if c in hashmap:
                j = hashmap[c]
                for k in range(prev, j + 1):
                    hashmap.pop(s[k])
                prev = j + 1
            hashmap[c] = i
        result = max(result, len(hashmap))
        return result
