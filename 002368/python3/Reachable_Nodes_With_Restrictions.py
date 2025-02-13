from typing import List


class Node:
    def __init__(self, val=0, restrict=False):
        self.val = val
        self.restrict = restrict
        self.neighbours = list()

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        nodemap = {i: Node(val=i) for i in range(n)}
        for val in restricted:
            node = nodemap[val]
            node.restrict = True
        for n1, n2 in edges:
            node1 = nodemap[n1]
            node2 = nodemap[n2]
            node1.neighbours.append(node2)
            node2.neighbours.append(node1)
        
        visit = set()
        
        def dfs(node: Node):
            visit.add(node.val)
            for neighbour in node.neighbours:
                if neighbour.val in visit or neighbour.restrict:
                    continue
                dfs(neighbour)

        dfs(nodemap[0])
        return len(visit)
