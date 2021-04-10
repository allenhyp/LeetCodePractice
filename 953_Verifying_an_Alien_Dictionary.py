class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {c: chr(i + ord('a')) for i, c in enumerate(order)}
        converted = [''.join([lookup[c] for c in w]) for w in words]
        for i in range(1, len(converted)):
            if converted[i - 1] > converted[i]:
                return False
        return True
