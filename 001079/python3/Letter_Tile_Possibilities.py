from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = list(tiles)
        tiles.sort()
        tiles = "".join(tiles)
        result = list()
        stack = list()
        
        def dfs(i: int):
            if i == len(tiles):
                result.append("".join(stack))
                return
            stack.append(tiles[i])
            dfs(i + 1)
            stack.pop()
            j = 0
            while i + j < len(tiles) and tiles[i + j] == tiles[i]:
                j += 1
            dfs(i + j)
            
        dfs(0)
        result = result[:-1]

        def perm(s: str) -> List[str]:
            letterCountMap = dict()
            for c in s:
                letterCountMap[c] = letterCountMap.get(c, 0) + 1
            result = list()
            stack = list()

            def dfs1(i: int):
                if i == len(s):
                    result.append("".join(stack))
                    return
                for l, c in letterCountMap.items():
                    if c == 0:
                        continue
                    stack.append(l)
                    letterCountMap[l] -= 1
                    dfs1(i + 1)
                    letterCountMap[l] += 1
                    stack.pop()

            dfs1(0)
            return result

        num = 0
        for r in result:
            res = perm(r)
            # print(res)
            num += len(res)
        return num
