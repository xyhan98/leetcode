from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        result = 0
        for p, c in zip(price, needs):
            result += p * c
        hashmap = dict()
        for offer in special:
            hashmap[tuple(offer)] = hashmap.get(tuple(offer), 0) + 1
        for i, need in enumerate(needs):
            offer = [0 for _ in range(len(price) + 1)]
            offer[-1] = price[i]
            offer[i] = 1
            hashmap[tuple(offer)] = hashmap.get(tuple(offer), 0) + need
        # print(hashmap)

        stack = [0 for _ in price]

        def dfs(cost: int):
            for count, need in zip(stack, needs):
                if count > need:
                    return
            if sum(stack) == sum(needs):
                nonlocal result
                result = min(result, cost)
                return
            for offer, num in hashmap.items():
                # if num == 0:
                #     continue
                # hashmap[offer] -= 1
                for i, c in enumerate(offer[:-1]):
                    stack[i] += c
                dfs(cost + offer[-1])
                for i, c in enumerate(offer[:-1]):
                    stack[i] -= c
                # hashmap[offer] += 1
        
        dfs(0)
        return result

s = Solution()
s.shoppingOffers([4,3,2,9,8,8], [[1,5,5,1,4,0,18],[3,3,6,6,4,2,32]], [6,5,5,6,4,1])
# Time Limit Exceeded (Backtracking)
