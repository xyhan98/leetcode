from typing import List


class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbours = list()

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        nodemap = {i: Node(val=i) for i in range(len(edges) + 1)}
        for n1, n2 in edges:
            node1 = nodemap[n1]
            node2 = nodemap[n2]
            node1.neighbours.append(node2)
            node2.neighbours.append(node1)
        
        visit = set()
        result = 0

        def dfs(node: Node) -> int:
            visit.add(node.val)
            children = list()
            for neighbour in node.neighbours:
                if neighbour.val in visit:
                    continue
                count = dfs(neighbour)
                children.append(count)
            nonlocal result
            if not children:
                result += 1
                return 1
            if all(map(lambda x: x == children[0], children)):
                result += 1
            return sum(children) + 1

        dfs(nodemap[0])
        return result
