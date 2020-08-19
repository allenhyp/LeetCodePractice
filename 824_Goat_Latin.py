class Solution:
    def __init__(self):
        self.vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i in range(len(words)):
            if words[i][0] not in self.vowel:
                words[i] = words[i][1:] + words[i][0]
            words[i] += 'ma' + 'a' * (i + 1)
        return ' '.join(words)
