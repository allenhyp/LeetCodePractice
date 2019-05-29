class Solution:        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        roots, dists, res = {}, {}, []
        def find(s):
            if s not in roots.keys():
                roots[s] = s
                dists[s] = 1.0
                return s
            if roots[s] == s:
                return s
            parent = roots[s]
            roots[s] = find(parent)
            dists[s] *= dists[parent]
            return roots[s]
        
        for i, e in enumerate(equations):
            p1, p2 = find(e[0]), find(e[1])
            roots[p1] = p2
            dists[p1] = dists[e[1]] * values[i] / dists[e[0]]
        for i, q in enumerate(queries):
            if q[0] not in roots.keys() or q[1] not in roots.keys():
                res.append(-1)
                continue
            p1, p2 = find(q[0]), find(q[1])
            if p1 != p2:
                res.append(-1)
            else:
                res.append(dists[q[0]] / dists[q[1]])
        return res
