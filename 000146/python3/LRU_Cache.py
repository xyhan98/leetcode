class Node:
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict()
        self.least = Node()
        self.recent = Node()
        self.least.nxt = self.recent
        self.recent.prev = self.least

    def get(self, key: int) -> int:
        node = self.hashMap.get(key)
        if not node:
            return -1
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
        node.nxt = self.recent
        node.prev = self.recent.prev
        node.prev.nxt = node
        self.recent.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if len(self.hashMap) < self.capacity:
            if key not in self.hashMap:
                node = Node(key=key, val=value, prev=self.recent.prev, nxt=self.recent)
                node.prev.nxt = node
                self.recent.prev = node
                self.hashMap[key] = node
            else:
                node = self.hashMap.get(key)
                node.val = value
                node.nxt.prev = node.prev
                node.prev.nxt = node.nxt
                node.nxt = self.recent
                node.prev = self.recent.prev
                node.prev.nxt = node
                self.recent.prev = node
        else:
            if key in self.hashMap:
                node = self.hashMap.get(key)
                node.val = value
                node.nxt.prev = node.prev
                node.prev.nxt = node.nxt
                node.nxt = self.recent
                node.prev = self.recent.prev
                node.prev.nxt = node
                self.recent.prev = node
            else:
                node = self.least.nxt
                k = node.key
                self.hashMap.pop(k)
                self.least.nxt = node.nxt
                node.nxt.prev = self.least
                node.key = key
                node.val = value
                node.nxt = self.recent
                node.prev = self.recent.prev
                node.prev.nxt = node
                self.recent.prev = node
                self.hashMap[key] = node
