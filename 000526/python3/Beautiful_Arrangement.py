class Solution:
    def countArrangement(self, n: int) -> int:
        result = 0
        hashmap = {i: 1 for i in range(1, n + 1)}

        def dfs(i: int):
            if i == n:
                nonlocal result
                result += 1
                return
            for k, v in hashmap.items():
                if v == 0:
                    continue
                if (k >= i + 1 and k % (i + 1) == 0) or (k < i + 1 and (i + 1) % k == 0):
                    hashmap[k] = 0
                    dfs(i + 1)
                    hashmap[k] = 1

        dfs(0)
        return result
