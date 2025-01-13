from typing import List


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        perms = list()
        stack = list()

        def dfs(i: int):
            if i == 7:
                perms.append("".join(stack))
                return
            for _ in range(i):
                stack.append(str(i))
            dfs(i + 1)
            for _ in range(i):
                stack.pop()
            dfs(i + 1)
        
        dfs(1)
        # print(perms)
        perms = sorted(list(map(int, [p for p in perms if 0 < len(p) <= 7])))
        # print(perms)

        results = list()

        def perm(num: int) -> List[int]:
            s = str(num)
            hashmap = dict()
            for c in s:
                hashmap[c] = hashmap.get(c, 0) + 1
            if len(hashmap) == 1:
                return [num]
            result = list()
            stack = list()

            def dfs(j: int):
                if j == len(s):
                    result.append(int("".join(stack)))
                    return
                for k, c in hashmap.items():
                    if c == 0:
                        continue
                    hashmap[k] -= 1
                    stack.append(k)
                    dfs(j + 1)
                    stack.pop()
                    hashmap[k] += 1
            
            dfs(0)
            return result

        for p in perms:
            res = perm(p)
            results.extend(res)
        results.sort()
        # print(results)

        i, j = 0, len(results) - 1
        while i <= j:
            mid = (i + j) // 2
            if results[mid] == n:
                return results[mid + 1]
            elif results[mid] < n:
                i = mid + 1
            else:
                j = mid - 1
        return results[i]

s = Solution()
s.nextBeautifulNumber(16407)
s.nextBeautifulNumber(49575)