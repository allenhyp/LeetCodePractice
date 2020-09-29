from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter, res = Counter(chars), 0
        for word in words:
            for c, n in Counter(word).items():
                if counter[c] < n:
                    break
            else:
                res += len(word)
        return res
