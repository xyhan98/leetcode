class Solution:
    def smallestNumber(self, pattern: str) -> str:
        hashmap = {i: 1 for i in range(1, 10)}
        stack = list()

        def dfs(i: int) -> bool:
            if i == len(pattern):
                return True
            for j, c in hashmap.items():
                if c == 0:
                    continue
                if (i == -1 or 
                    (pattern[i] == "I" and stack[-1] < j) or 
                    (pattern[i] == "D" and stack[-1] > j)):
                    hashmap[j] -= 1
                    stack.append(j)
                    if dfs(i + 1):
                        return True
                    stack.pop()
                    hashmap[j] += 1
            return False
        
        dfs(-1)
        return "".join(map(str, stack))
