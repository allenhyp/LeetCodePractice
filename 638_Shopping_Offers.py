class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dic, n = {}, len(price)
        def dfs(need):
            val = sum(need[i] * price[i] for i in range(n))
            for s in special:
                tmp = []
                for i in range(n):
                    cut = need[i] - s[i]
                    if cut < 0:
                        tmp = None
                        break
                    else:
                        tmp.append(cut)
                else:
                    val = min(val, dic.get(tuple(tmp), dfs(tmp)) + s[-1])
                    dic[tuple(tmp)] = val
            return val
        return dfs(needs)
