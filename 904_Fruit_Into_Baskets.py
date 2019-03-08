class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        types, max_quantity, i = {}, 0, 0
        for j, fruit_type in enumerate(tree):
            types[fruit_type] = types.get(fruit_type, 0) + 1
            while len(types) > 2:
                types[tree[i]] -= 1
                if types[tree[i]] == 0:
                    del types[tree[i]]
                i += 1
            max_quantity = max(max_quantity, j - i + 1)
        return max_quantity

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        if n < 3:
            return n
        f1 = f2 = n2 = 0
        res = current = 0
        for t in tree:
            if t == f2:
                n2 += 1
                current += 1
            elif t == f1:
                n2 = 1
                current += 1
                f1, f2 = f2, f1
            else:
                current = n2 + 1
                n2 = 1
                f1, f2 = f2, t
            res = max(res, current)
        return res
