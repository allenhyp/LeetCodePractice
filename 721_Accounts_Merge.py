class UF:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
    
    def union(self, parent, child):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(ownership[email], i)
                ownership[email] = i
        
        ret = collections.defaultdict(list)
        for email, owner in ownership.items():
            ret[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ret.items()]
