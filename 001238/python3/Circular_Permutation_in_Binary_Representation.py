from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        binNumMap = dict()
        total = 2**n - 1

        def binRep(num: int) -> List[int]:
            copy = num
            bs = list()
            while copy > 0:
                b = copy % 2
                bs.append(b)
                copy = copy // 2
            bs.reverse()
            return [0] * (n - len(bs)) + bs
        
        for i in range(total + 1):
            bs = binRep(i)
            binNumMap[tuple(bs)] = i
        # print(binNumMap)

        stack = binRep(start)
        result = [binNumMap[tuple(stack)]]
        visit = {start}

        def dfs(i: int) -> bool:
            if i == total:
                first, last = binRep(result[0]), binRep(result[-1])
                return True if sum(map(lambda x: abs(x[0] - x[1]), zip(first, last))) == 1 else False
            for j in range(n):
                stack[j] = 1 - stack[j]
                num = binNumMap[tuple(stack)]
                if num not in visit:
                    visit.add(num)
                    result.append(num)
                    if dfs(i + 1):
                        return True
                    result.pop()
                    visit.remove(num)
                stack[j] = 1 - stack[j]
            return False
        
        dfs(0)
        return result
