from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        stack = list()

        def dfs(i: int, sum: int):
            if sum == target:
                    result.append(list(stack))
            if sum >= target or i == len(candidates):
                return
            stack.append(candidates[i])
            dfs(i, sum + candidates[i])
            stack.pop()
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return result
