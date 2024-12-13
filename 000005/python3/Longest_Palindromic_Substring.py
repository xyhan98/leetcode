class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def getPalindrome(p: int, q: int):
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1
            return s[p + 1:q]
            

        for i in range(len(s)):
            t = getPalindrome(i, i)
            if len(t) > len(result):
                result = t
            if i > 0 and s[i - 1] == s[i]:
                t = getPalindrome(i - 1, i)
                if len(t) > len(result):
                    result = t
        
        # print(result)
        return result
