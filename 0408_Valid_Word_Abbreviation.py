class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] != abbr[j]:
                    return False
                else:
                    i, j = i + 1, j + 1
            elif abbr[j] == '0':
                return False
            else:
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                i += num

        return i == len(word) and j == len(abbr)
