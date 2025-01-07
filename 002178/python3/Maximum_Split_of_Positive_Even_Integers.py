from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = list()
        if finalSum % 2 != 0:
            return result
        copy = finalSum
        prev = 0
        while copy > prev:
            prev += 2
            result.append(prev)
            copy -= prev
        if copy > 0:
            result[-1] += copy
        return result
