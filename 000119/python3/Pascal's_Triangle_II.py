from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        curr = [1, 1]
        if rowIndex == 0:
            return prev
        if rowIndex == 1:
            return curr
        i = 2
        while i <= rowIndex:
            prev = curr
            curr = [1]
            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            curr.append(1)
            i += 1
        return curr
