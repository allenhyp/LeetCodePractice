from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        n = len(beginWord)
        lookup = defaultdict(list)
        for word in wordList:
            for i in range(n):
                mask = word[:i] + '*' + word[i + 1:]
                lookup[mask].append(word)
    
        wordSet = set(wordList) 
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = defaultdict(list)
            for word in layer:
                if word == endWord: 
                    return layer[word]
                for i in range(n):
                    mask = word[:i] + '*' + word[i + 1:]
                    for nextWord in lookup[mask]:
                        if nextWord in wordSet:
                            newLayer[nextWord] += [past + [nextWord] for past in layer[word]]
                        
            wordSet -= set(newLayer.keys())
            layer = newLayer

        return []
