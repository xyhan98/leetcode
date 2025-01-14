import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hashset = {(0, 0, 0)}
        list = [(1, 0, 0, 0)]
        heapq.heapify(list)
        i, num = 1, 0
        while i <= n:
            num, two, three, five = heapq.heappop(list)
            if (two + 1, three, five) not in hashset:
                hashset.add((two + 1, three, five))
                heapq.heappush(list, (num * 2, two + 1, three, five))
            if (two, three + 1, five) not in hashset:
                hashset.add((two, three + 1, five))
                heapq.heappush(list, (num * 3, two, three + 1, five))
            if (two, three, five + 1) not in hashset:
                hashset.add((two, three, five + 1))
                heapq.heappush(list, (num * 5, two, three, five + 1))
            i += 1
        return num
