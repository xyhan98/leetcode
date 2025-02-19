from typing import List


class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = list()

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        nodemap = {i: Node(val=i) for i in range(n)}
        for n1, n2 in roads:
            node1 = nodemap[n1]
            node2 = nodemap[n2]
            node1.children.append(node2)
            node2.children.append(node1)
        
        visit = set()
        result = 0
        
        def dfs(node: Node) -> int:
            visit.add(node.val)
            lst = list()
            for neighbour in node.children:
                if neighbour.val in visit:
                    continue
                c = dfs(neighbour)
                lst.append(c)
            count = sum(lst) + 1 if lst else 1
            nonlocal result
            if node.val != 0:
                if count % seats == 0:
                    result += count // seats
                else:
                    result += count // seats + 1
            return count

        dfs(nodemap[0])
        return result
