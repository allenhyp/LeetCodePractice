class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            if N == 1:
                return 1
            return -1
        trusted_dic, trust_dic = {}, {}
        for t in trust:
            trusted_dic[t[1]] = trusted_dic.get(t[1], 0) + 1
            trust_dic[t[0]] = trust_dic.get(t[0], []) + [t[1]]
        town_judge = []
        for key in trusted_dic:
            if trusted_dic[key] == N - 1:
                town_judge.append(key)
        print(trust_dic)
        if len(town_judge) != 1 or town_judge[0] in trust_dic.keys():
            return -1
        return town_judge[0]
