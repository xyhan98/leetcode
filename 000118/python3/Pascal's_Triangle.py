from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1, 1])
        for _ in range(3, numRows + 1):
            prev = result[-1]
            curr = [1]
            for i in range(1, len(prev)):
                curr.append(prev[i - 1] + prev[i])
            curr.append(1)
            result.append(curr)
        return result
