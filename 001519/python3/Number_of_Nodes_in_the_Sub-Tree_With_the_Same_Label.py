from typing import List, Optional


class Node:
    def __init__(self, val=0, label=None):
        self.val = val
        self.children = list()
        self.label = label

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        nodemap = {i: Node(val=i, label=labels[i]) for i in range(n)}
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
        result = [0 for _ in range(n)]
        
        def dfs(node: Optional[Node]) -> dict:
            hashmap = dict()
            for child in node.children:
                d = dfs(child)
                for k, v in d.items():
                    hashmap[k] = hashmap.get(k, 0) + v
            label = node.label
            hashmap[label] = hashmap.get(label, 0) + 1
            result[node.val] = hashmap[label]
            return hashmap
        
        dfs(nodemap[0])
        return result
