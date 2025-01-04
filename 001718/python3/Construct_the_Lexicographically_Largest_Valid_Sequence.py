from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        hashmap = {i: 2 for i in range(n, 1, -1)}
        hashmap[1] = 1
        count = 2 * n - 1
        stack = [0 for _ in range(count)]

        def dfs(i: int) -> bool:
            if i == count:
                return True
            for j, c in hashmap.items():
                if c == 0:
                    continue
                if j != 1 and i + j < count and stack[i + j] == 0:
                    stack[i] = j
                    stack[i + j] = j
                    hashmap[j] = 0
                    k = 0
                    while i + k < count and stack[i + k] != 0:
                        k += 1
                    if dfs(i + k):
                        return True
                    stack[i] = 0
                    stack[i + j] = 0
                    hashmap[j] = 2
                elif j == 1:
                    stack[i] = 1
                    hashmap[j] = 0
                    k = 0
                    while i + k < count and stack[i + k] != 0:
                        k += 1
                    if dfs(i + k):
                        return True
                    stack[i] = 0
                    hashmap[j] = 1
                    
            return False

        dfs(0)
        return stack
