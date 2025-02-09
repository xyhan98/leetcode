from typing import List, Optional, Tuple


class Node:
    def __init__(self, val=0, has=False):
        self.val = val
        self.children= list()
        self.has = has

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodemap = {i: Node(val=i, has=hasApple[i]) for i in range(n)}
        edgemap = {i: list() for i in range(n)}
        for n1, n2 in edges:
            edgemap[n1].append(n2)
            edgemap[n2].append(n1)
        
        queue = [0]
        visit = {0}
        while queue:
            nxt = list()
            for i in queue:
                root = nodemap[i]
                for j in edgemap[i]:
                    if j in visit:
                        continue
                    visit.add(j)
                    node = nodemap[j]
                    root.children.append(node)
                    nxt.append(j)
            queue = nxt
        
        del queue, visit, edgemap

        def dfs(node: Optional[Node], total: int) -> Tuple[bool, int]:
            has = False
            for child in node.children:
                b, total = dfs(child, total + 1)
                has = has or b
            has = has or node.has
            return has, total + (1 if has else -1)

        b, total = dfs(nodemap[0], 0)
        return total + (-1 if b else 1)
