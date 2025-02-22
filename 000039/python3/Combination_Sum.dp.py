from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = [list() for _ in range(target + 1)]
        cache[0].append(list())
        for candidate in candidates:
            for i in range(1, target + 1):
                if i < candidate:
                    continue
                else:
                    for lst in cache[i - candidate]:
                        cache[i].append(lst + [candidate])
        return cache[-1]
