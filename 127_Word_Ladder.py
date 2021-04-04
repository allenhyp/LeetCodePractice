from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        lookup = defaultdict(list)
        for word in wordList:
            for i in range(n):
                mask = word[:i] + '*' + word[i + 1:]
                lookup[mask].append(word)
        
        wordSet = set(wordList)
        layer = set([beginWord])
        steps = 1
        
        while layer:
            nextLayer = set()
            for word in layer:
                if word == endWord:
                    return steps
                for i in range(n):
                    mask = word[:i] + '*' + word[i + 1:]
                    for nextWord in lookup[mask]:
                        if nextWord in wordSet:
                            nextLayer.add(nextWord)
            wordSet -= nextLayer
            layer = nextLayer
            steps += 1
        
        return 0
