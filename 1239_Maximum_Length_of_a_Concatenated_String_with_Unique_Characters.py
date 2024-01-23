class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = []
        for s in arr:
            u = set(s)
            if len(u) == len(s):
                unique.append(u)
        
        concat = [set()]
        for u in unique:
            for c in concat:
                if not u & c:
                    concat.append(u | c)
        
        return max([len(c) for c in concat])
