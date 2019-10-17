class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        res = sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))[:k]
        return list(res[i][0] for i in range(len(res)))
