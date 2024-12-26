from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = list()
        stack = list()

        def dfs(i: int):
            stack.append(i)
            if i == len(graph) - 1:
                result.append(list(stack))
            if graph[i] != []:
                for j in graph[i]:
                    dfs(j)
            stack.pop()
        
        dfs(0)
        return result

s = Solution()
s.allPathsSourceTarget([[2],[],[1]])
