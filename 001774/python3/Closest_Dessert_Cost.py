from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        cache = dict()
        stack = [0 for _ in toppingCosts]

        def dfs(i: int):
            if i == len(stack):
                cache[tuple(stack)] = sum(map(lambda x: x[0] * x[1], zip(stack, toppingCosts)))
                return
            for j in range(3):
                stack[i] = j
                dfs(i + 1)
        
        dfs(0)
        # print(cache)
        toppings = set(cache.values())
        results = set()
        toppingCost = sorted(list(toppings))
        # print(toppingCost)
        for base in baseCosts:
            if target - base in toppings:
                return target
            i, j = 0, len(toppingCost) - 1
            while i <= j:
                mid = (i + j) // 2
                if toppingCost[mid] < target - base:
                    i = mid + 1
                else:
                    j = mid - 1
            if 0 <= i < len(toppingCost):
                results.add(base + toppingCost[i])
            if 0 <= j < len(toppingCost):
                results.add(base + toppingCost[j])
        diff = min(map(lambda x: abs(x - target), sorted(list(results))))
        return target - diff if target - diff in results else target + diff
