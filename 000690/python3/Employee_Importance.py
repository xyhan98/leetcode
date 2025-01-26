from typing import List, Optional


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idmap = dict()
        for employee in employees:
            idmap[employee.id] = employee
        
        def dfs(node: Optional[Employee]) -> int:
            importance = node.importance
            for id in node.subordinates:
                importance += dfs(idmap[id])
            return importance
        
        return dfs(idmap[id])
        