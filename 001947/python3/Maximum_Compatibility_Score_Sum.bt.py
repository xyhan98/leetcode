from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        cache = dict()
        for i, student in enumerate(students):
            for j, mentor in enumerate(mentors):
                cache[(i, j)] = sum(map(lambda x: int(x[0] - x[1] == 0), zip(student, mentor)))
        # print(cache)
        hashmap = {j: 1 for j in range(m)}
        result = 0
        stack = list()

        def dfs(i: int):
            if i == m:
                nonlocal result
                result = max(result, sum(stack))
                return
            for j, c in hashmap.items():
                if c == 0:
                     continue
                hashmap[j] = 0
                stack.append(cache[(i, j)])
                dfs(i + 1)
                stack.pop()
                hashmap[j] = 1
        
        dfs(0)
        return result
