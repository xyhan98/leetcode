from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        result = list()

        def getPoints(t: str) -> List[str]:
            points = list()
            if len(t) == 1:
                points.append(t)
            elif len(t) > 1:
                if t[0] == "0":
                    points.append(f"0.{t[1:]}")
                elif t[-1] == "0":
                    points.append(t)
                else:
                    for i in range(1, len(t)):
                        points.append(f"{t[:i]}.{t[i:]}")
                    points.append(t)
            return points

        s = s[1:-1]
        for i in range(1, len(s)):
            p = s[:i]
            q = s[i:]
            if len(p) > 1 and p[0] == "0" and p[-1] == "0":
                continue
            if len(q) > 1 and q[0] == "0" and q[-1] == "0":
                continue
            xs = getPoints(p)
            ys = getPoints(q)
            for x in xs:
                for y in ys:
                    coordinate = f"({x}, {y})"
                    result.append(coordinate)
        return result
