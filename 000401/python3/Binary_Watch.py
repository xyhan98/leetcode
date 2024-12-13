from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # H: 1 0 1 1 (11)
        # M: 1 1 1 0 1 1 (59)
        # maximum turnedOn = 3 + 5 = 8
        result = list()
        if turnedOn > 8:
            return result
        if turnedOn == 0:
            return ["0:00"]
        cache = {i: list() for i in range(1, 6)}
        for i in range(1, 60):
            j, k = 0, i
            while k > 0:
                j += k % 2
                k = k // 2
            cache[j].append(i)
        # print(cache)
        for i in range(min(3, turnedOn) + 1):
            if turnedOn - i > 5:
                continue
            elif turnedOn - i == 0:
                ms = ["00"]
            else:
                ms = [str(m) if m > 9 else f"0{m}" for m in cache[turnedOn - i]]
            if i == 0:
                hs = [0]
            else:
                hs = [h for h in cache[i] if h < 12]
            for h in hs:
                for m in ms:
                    result.append(f"{h}:{m}")
        return result
