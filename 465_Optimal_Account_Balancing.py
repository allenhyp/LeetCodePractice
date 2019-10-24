class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = collections.defaultdict(int)
        for source, target, amount in transactions:
            balances[source] -= amount
            balances[target] += amount

        balances_clear = collections.defaultdict(int)
        base = 0
        for v in balances.values():
            if v == 0:
                continue
            if -v in balances_clear:
                balances_clear[-v] -= 1
                base += 1
            else:
                balances_clear[v] += 1
                
        net_profit = []
        for key, val in balances_clear.items():
            net_profit.extend([key] * val)
        
        n = len(net_profit)
        
        def dfs(i):
            if i >= n - 1:
                return 0
            if net_profit[i] == 0:
                return dfs(i + 1)
            
            p = net_profit[i]
            res = math.inf
            seen = set()
            for j in range(i + 1, n):
                if net_profit[j] * p < 0 and net_profit[j] not in seen:
                    net_profit[j] += p
                    res = min(res, 1 + dfs(i + 1))
                    net_profit[j] -= p
                    seen.add(net_profit[j])
                    if net_profit[i] + net_profit[j] == 0:
                        return res
            return res
        
        return dfs(0) + base