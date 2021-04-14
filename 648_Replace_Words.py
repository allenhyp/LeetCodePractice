class TrieNode:
        def __init__(self):
            self.endOfWord = False
            self.complete = ""
            self.children = {}

class Solution:        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for i, c in enumerate(word):
                if c not in curr.children:
                    curr.children[c] = TrieNode()                    
                curr = curr.children[c]
                if i == len(word) - 1:
                    curr.complete = word
                    curr.endOfWord = True
        
        res = []
        for word in sentence.split():
            curr = root
            found = False
            for c in word:
                if c in curr.children:
                    curr = curr.children[c]
                    if curr.endOfWord:
                        res.append(curr.complete)
                        found = True
                        break
                else:
                    break
            if not found:
                res.append(word)
        return " ".join(res)
