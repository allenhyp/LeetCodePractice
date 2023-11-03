from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        for char, occurance in r.items():
            if char not in m or m[char] < occurance:
                return False
        return True
