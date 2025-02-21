from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            copy = i
            count = 0
            while copy > 0:
                count += copy % 2
                copy = copy // 2
            result[i] = count
        return result
