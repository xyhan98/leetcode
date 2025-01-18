class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {n}
        while n != 1:
            digits = sum(map(lambda x: int(x) ** 2, str(n)))
            if digits in nums:
                return False
            nums.add(digits)
            n = digits
        return True
