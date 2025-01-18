class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = dict()
        reversed = dict()
        for s1, t1 in zip(s, t):
            if s1 in hashmap:
                if hashmap[s1] != t1:
                    return False
            else:
                if t1 in reversed:
                    if reversed[t1] != s1:
                        return False
                else:
                    hashmap[s1] = t1
                    reversed[t1] = s1
        return True
