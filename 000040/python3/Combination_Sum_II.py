from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        stack = list()

        def dfs(i: int, sum: int):
            if sum == target:
                result.append(list(stack))
            if i == len(candidates) or sum >= target:
                return
            stack.append(candidates[i])
            dfs(i + 1, sum + candidates[i])
            stack.pop()
            j = 0
            while i + j < len(candidates) and candidates[i] == candidates[i + j]:
                j += 1
            dfs(i + j, sum)
        
        dfs(0, 0)
        return result
