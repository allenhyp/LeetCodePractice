from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins, loses = defaultdict(int), defaultdict(int)
        for win, lose in matches:
            wins[win] += 1
            loses[lose] += 1
        
        ret = [[], []]
        for winner in sorted(wins.keys()):
            if winner not in loses:
                ret[0].append(winner)
        
        for loser in sorted(loses.keys()):
            if loses[loser] == 1:
                ret[1].append(loser)
        
        return ret
