class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        smap = dict()
        gmap = dict()
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                smap[s] = smap.get(s, 0) + 1
                gmap[g] = gmap.get(g, 0) + 1
        for g, c in gmap.items():
            if g in smap:
                cows += min(c, smap[g])
        return f"{bulls}A{cows}B"
