class Solution:
    def sortVowels(self, s: str) -> str:
        ret, v, indexes = [], [], []
        for i, c in enumerate(s):
            if c in "AEIOUaeiou":
                v.append(ord(c))
                indexes.append(i)
            ret.append(c)

        heapq.heapify(v)
        for index in indexes:
            ret[index] = chr(heapq.heappop(v))
        
        return ''.join(ret)
