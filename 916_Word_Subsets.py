from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        checkList = Counter()
        for b in B:
            checkList |= Counter(b)
        
        return [a for a in A if not checkList - Counter(a)]
