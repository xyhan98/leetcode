class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        two, three = 0, 0
        if n % 3 == 0:
            three = n // 3
        elif n % 3 == 1:
            three = n // 3 - 1
            two = 2
        else:
            three = n // 3
            two = 1
        return 2**two * 3**three
