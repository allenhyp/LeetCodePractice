class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        for i in range(len(A)):
            count = {}
            for c in A[i]:
                count[c] = (count.get(c, 0) << 1) + 1
            if i == 0:
                total_count = count
            else:
                for key, val in total_count.items():
                    if key in count:
                        total_count[key] = min(count[key], val)
                    else:
                        total_count[key] = 0
        res = []
        for key, val in total_count.items():
            while val > 0:
                res.append(key)
                val = val >> 1
        return res
