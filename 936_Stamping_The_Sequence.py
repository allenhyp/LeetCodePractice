class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        tn, sn = len(target), len(stamp)
        aim = ['*'] * tn
        cur = [c for c in target]
        res = []
        
        def replace(cur, stamp):
            for i in range(tn - sn + 1):
                k, j, match = i, 0, False
                while k < tn and j < sn and (cur[k] == '*' or cur[k] == stamp[j]):
                    if cur[k] != '*': match = True
                    k, j = k + 1, j + 1
                if j == sn and match:
                    for k in range(i, i + sn):
                        cur[k] = '*'
                    return i
            return -1
        
        while cur != aim:
            idx = replace(cur, stamp)
            if idx >= 0: res.append(idx)
            else: return []
        return res[::-1]
