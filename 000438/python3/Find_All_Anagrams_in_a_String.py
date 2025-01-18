from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pmap = dict()
        smap = dict()
        result = list()
        for c in p:
            pmap[c] = pmap.get(c, 0) + 1
        for c in s[:len(p)]:
            smap[c] = smap.get(c, 0) + 1
        if pmap == smap:
            result.append(0)
        for i, c in enumerate(s[len(p):], len(p)):
            t = s[i - len(p)]
            smap[t] -= 1
            if smap[t] == 0:
                smap.pop(t)
            smap[c] = smap.get(c, 0) + 1
            if pmap == smap:
                result.append(i - len(p) + 1)

        return result
        