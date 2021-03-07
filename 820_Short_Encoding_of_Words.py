class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = dict()
        leaves = []
        for word in set(words):
            curr = root
            for c in word[::-1]:
                curr[c] = curr = curr.get(c, dict())
            leaves.append((curr, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)
