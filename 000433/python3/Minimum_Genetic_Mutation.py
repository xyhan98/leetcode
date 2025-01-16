from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene not in bank:
            bank.append(startGene)
        hashmap = dict()
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if sum(map(lambda x: bool(x[0] != x[1]), zip(bank[i], bank[j]))) == 1:
                    if bank[i] not in hashmap:
                        hashmap[bank[i]] = list()
                    hashmap[bank[i]].append(bank[j])
                    if bank[j] not in hashmap:
                        hashmap[bank[j]] = list()
                    hashmap[bank[j]].append(bank[i])
        # print(hashmap)

        result = list()
        stack = [startGene]
        visit = set()

        def dfs():
            if len(stack) == len(bank):
                return
            for mutation in hashmap[stack[-1]]:
                if mutation in visit:
                    continue
                visit.add(mutation)
                stack.append(mutation)
                if mutation == endGene:
                    result.append(list(stack))
                else:
                    dfs()
                stack.pop()
                visit.remove(mutation)
        
        dfs()
        return min(map(len, result)) - 1 if result else -1
