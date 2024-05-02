class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        occ = collections.defaultdict(int)
        pre = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        croaking = 0
        ret = 0
        for i, c in enumerate(croakOfFrogs):
            if c == 'c':
                occ[c] += 1
                croaking += 1
            elif occ[pre[c]] <= occ[c]:
                return -1
            else:
                occ[c] += 1

            if c == 'k':
                croaking -= 1
            
            ret = max(ret, croaking)

        return -1 if croaking != 0 or any(occ[pre[k]] - occ[k] for k in pre.keys()) else ret
