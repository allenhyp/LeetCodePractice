class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last = 0
        ret = 0
        for row in bank:
            level = 0
            for d in row:
                level += 1 if d == '1' else 0
            if last and level > 0:
                ret += last * level
            last = level if level > 0 else last
        return ret
