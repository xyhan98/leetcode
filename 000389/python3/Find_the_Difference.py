class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tmap = dict()
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        for c in s:
            tmap[c] -= 1
            if tmap[c] == 0:
                tmap.pop(c)
        return list(tmap.keys())[0]
