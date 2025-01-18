class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = dict()
        for c in magazine:
            hashmap[c] = hashmap.get(c, 0) + 1
        for c in ransomNote:
            if c not in hashmap or hashmap[c] == 0:
                return False
            hashmap[c] -= 1
        return True
