class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isEligible(word):
            itr = iter(s)
            return all(c in itr for c in word)
        return min(list(filter(isEligible, d)) + [''], key=lambda x: (-len(x), x))
