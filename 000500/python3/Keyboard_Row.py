from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fst = set("qwertyuiop")
        snd = set("asdfghjkl")
        trd = set("zxcvbnm")
        result = list()
        for word in words:
            t = set(word.lower())
            for s in [fst, snd, trd]:
                if not (t - s):
                    result.append(word)
        return result
