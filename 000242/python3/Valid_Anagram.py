class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = dict()
        tmap = dict()
        for c in s:
            smap[c] = smap.get(c, 0) + 1
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        for k, v in smap.items():
            if k not in tmap or v != tmap[k]:
                return False
            tmap.pop(k)
        return not tmap
        