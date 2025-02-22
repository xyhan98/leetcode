from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cache = [list() for _ in range(target + 1)]
        cache[0].append(list())
        for candidate in candidates:
            for i in range(target, -1, -1):
                if i < candidate:
                    continue
                else:
                    for lst in cache[i - candidate]:
                        lst1 = lst + [candidate]
                        if lst1 not in cache[i]:
                            cache[i].append(lst1)
        return cache[-1]
