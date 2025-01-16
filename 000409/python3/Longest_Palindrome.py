class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = dict()
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        result = 0
        odd = 0
        for k, v in hashmap.items():
            if v % 2 == 0:
                result += v
            else:
                if odd >= v:
                    result += v - 1
                else:
                    if odd % 2 == 1:
                        result += odd - 1
                    odd = v
        result += odd
        return result
