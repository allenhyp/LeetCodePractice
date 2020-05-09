class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set(p[0] for p in paths)
        dests = set(p[1] for p in paths)
        return (dests - starts).pop()
