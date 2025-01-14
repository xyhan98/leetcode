class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pmap = dict()
        smap = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i, p in enumerate(pattern):
            if p in pmap:
                if pmap[p] != s[i]:
                    return False
            else:
                if s[i] in smap:
                    return False
                pmap[p] = s[i]
                smap[s[i]] = p
        return True
