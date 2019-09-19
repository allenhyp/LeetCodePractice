class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        for h, n in sorted(people, key=lambda p: (-p[0], p[1])):
            res.insert(n, [h, n])
        return res
