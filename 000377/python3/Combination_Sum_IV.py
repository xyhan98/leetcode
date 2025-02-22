from typing import List


class Solution:
    # Memory Limit Exceeded
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [list() for _ in range(target + 1)]
        cache[0].append(dict())
        for num in nums:
            for i in range(1, target + 1):
                if i < num:
                    continue
                else:
                    for d in cache[i - num]:
                        d = dict(d)
                        d[num] = d.get(num, 0) + 1
                        cache[i].append(d)
        
        result = list()
        stack = list()

        def dfs(i: int, d: dict, count: int):
            if i == count:
                result.append(list(stack))
                return
            for k, v in d.items():
                if v == 0:
                    continue
                stack.append(k)
                d[k] -= 1
                dfs(i + 1, d, count)
                d[k] += 1
                stack.pop()

        for d in cache[-1]:
            dfs(0, d, sum(d.values()))
        return len(result)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0 for _ in range(target + 1)]
        cache[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i < num:
                    continue
                else:
                    cache[i] += cache[i - num]
        return cache[-1]
