from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > (1 + 9) * 9 // 2:
            return list()
        cache = [list() for _ in range(n + 1)]
        cache[0].append(list())
        for i in range(1, 10):
            for j in range(n, -1, -1):
                if j < i:
                    continue
                else:
                    for lst in cache[j - i]:
                        cache[j].append(lst + [i])
        return [lst for lst in cache[-1] if len(lst) == k]
