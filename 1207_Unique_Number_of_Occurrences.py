from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        return len(occurrences.keys()) == len(set(occurrences.values()))
