class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = dict()
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        vals = [(v, k) for k, v in hashmap.items()]
        vals.sort(reverse=True)
        vals = [f"{c}" * v for v, c in vals]
        return "".join(vals)
