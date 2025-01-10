class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        hashset = {"1"}

        def binRep(n: int) -> str:
            result = list()
            while n > 0:
                result.append(str(n % 2))
                n //= 2
            result.reverse()
            return "".join(result)

        val = 1
        for _ in range(7):
            val *= 5
            t = binRep(val)
            hashset.add(t)
        # print(hashset)

        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(s):
                result.append(list(stack))
                return
            for j in range(1, len(s) + 1 - i):
                c = s[i:i + j]
                if c in hashset:
                    stack.append(c)
                    dfs(i + j)
                    stack.pop()
        
        dfs(0)
        return min(map(len, result)) if result else -1
