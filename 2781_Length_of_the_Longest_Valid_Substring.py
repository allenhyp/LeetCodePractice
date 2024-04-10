_MAX_FORBIDDEN_LENGTH = 10
class Trie:
    def __init__(self, key, eow=False):
        self.key = key
        self.next = {}
        self.eow = eow
        
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        root = Trie('#')
        for f in forbidden:
            node = root
            for c in f:
                if c not in node.next:
                    node.next[c] = Trie(c)
                node = node.next[c]
            node.eow = True
        
        n = len(word)
        last = n
        ret = 0
        for i in range(n-1, -1, -1):
            node = root
            for j in range(i, min(i + _MAX_FORBIDDEN_LENGTH, last)):
                if word[j] not in node.next:
                    break
                node = node.next[word[j]]
                if node.eow:
                    last = j
                    break
            ret = max(ret, last - i)

        return ret
