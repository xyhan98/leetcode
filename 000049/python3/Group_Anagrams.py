from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = [("".join(sorted(s)), i) for i, s in enumerate(strs)]
        copy.sort()
        results = list()
        i = 0
        while i < len(copy):
            j = 0
            anagrams = list()
            while i + j < len(copy) and copy[i + j][0] == copy[i][0]:
                anagrams.append(strs[copy[i + j][1]])
                j += 1
            i += j
            results.append(anagrams)
        return results
