class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result = 1
        if n == 0:
            return result
        digits = 9
        acc = 9
        i = 0
        while i < n:
            result += acc
            acc *= digits - i
            i += 1
        return result
