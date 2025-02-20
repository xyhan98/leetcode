from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = dict()

        def dfs(s: str) -> List[int]:
            if s.isdigit():
                return [int(s)]
            if s in cache:
                return cache[s]
            res = list()
            for i in range(len(s)):
                if s[i].isdigit():
                    continue
                ls = dfs(s[:i])
                rs = dfs(s[i + 1:])
                for l in ls:
                    for r in rs:
                        if s[i] == "+":
                            res.append(l + r)
                        elif s[i] == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
            cache[s] = res
            return res
        
        return dfs(expression)
