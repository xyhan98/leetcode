import math
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        1048576 (2**20)
        1000000 (10**6)
        """
        cache = dict()
        cache[0] = 1
        for i in range(1, 21):
            cache[i] = cache[i - 1] * 2
        height = 0
        while cache[height] <= label:
            height += 1
        height -= 1
        result = [label]
        indicies = list()
        if height % 2 == 0:
            indicies.append(label)
        else:
            indicies.append(cache[height + 1] - 1 - label + cache[height])
        for i in range(height - 1, -1, -1):
            nxt = indicies[-1]
            if nxt % 2 == 0:
                indicies.append(nxt // 2)
            else:
                indicies.append((nxt - 1) // 2)
            if i % 2 == 0:
                result.append(indicies[-1])
            else:
                result.append(cache[i + 1] - 1 - (indicies[-1] - cache[i]))
        result.reverse()
        return result
