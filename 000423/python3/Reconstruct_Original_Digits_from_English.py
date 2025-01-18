class Solution:
    def originalDigits(self, s: str) -> str:
        """
        zero - z
        one -- o
        two - w
        three -- t
        four - u
        five -- f
        six - x
        seven -- s
        eight - g
        nine

        'zeroonetwothreefourfivesixseveneightnine'

        {'z': 1, 'e': 9, 'r': 3, 'o': 4, 'n': 4, 't': 3, 'w': 1, 'h': 2, 'f': 2, 'u': 1, 'i': 4, 'v': 2, 's': 2, 'x': 1, 'g': 1}
        """

        smap = dict()
        for c in s:
            smap[c] = smap.get(c, 0) + 1
        
        rmap = {i: 0 for i in range(10)}

        if "z" in smap:
            count = smap["z"]
            rmap[0] = count
            for c in "zero":
                smap[c] -= count
        if "w" in smap:
            count = smap["w"]
            rmap[2] = count
            for c in "two":
                smap[c] -= count
        if "u" in smap:
            count = smap["u"]
            rmap[4] = count
            for c in "four":
                smap[c] -= count
        if "x" in smap:
            count = smap["x"]
            rmap[6] = count
            for c in "six":
                smap[c] -= count
        if "g" in smap:
            count = smap["g"]
            rmap[8] = count
            for c in "eight":
                smap[c] -= count

        if "o" in smap and smap["o"] > 0:
            count = smap["o"]
            rmap[1] = count
            for c in "one":
                smap[c] -= count
        if "t" in smap and smap["t"] > 0:
            count = smap["t"]
            rmap[3] = count
            for c in "three":
                smap[c] -= count
        if "f" in smap and smap["f"] > 0:
            count = smap["f"]
            rmap[5] = count
            for c in "five":
                smap[c] -= count
        if "s" in smap and smap["s"] > 0:
            count = smap["s"]
            rmap[7] = count
            for c in "seven":
                smap[c] -= count
        if "i" in smap and smap["i"] > 0:
            count = smap["i"]
            rmap[9] = count
        
        result = [f"{k}" * v for k, v in rmap.items() if v != 0]
        return "".join(result)
        