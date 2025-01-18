from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        hashmap = {i: [0 for _ in range(len(points))] for i in range(len(points))}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                hashmap[i][j] = d
                hashmap[j][i] = d
        # print(hashmap)
        result = 0
        for vals in hashmap.values():
            pmap = dict()
            for val in vals:
                pmap[val] = pmap.get(val, 0) + 1
            for k, v in pmap.items():
                if v >= 2:
                    result += v * (v - 1)
        return result
