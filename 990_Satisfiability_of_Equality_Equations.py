class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        uf = {a: a for a in 'abcdefghijklmnopqrstuvwxyz'}
        equations.sort(key=lambda e: e[1] == '!')
        def union_find(x):
            if x != uf[x]:
                uf[x] = union_find(uf[x])
            return uf[x]
        for item in equations:
            if item[1] == '=':
                uf[union_find(item[0])] = union_find(item[3])
            else:
                if union_find(item[0]) == union_find(item[3]):
                    return False
        return True
