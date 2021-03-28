from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        freq = [0] * 10
        for unique, i in [('z', 0), ('w', 2), ('u', 4), ('x', 6), ('g', 8),
                          ('o', 1), ('t', 3), ('f', 5), ('s', 7), ('i', 9)]:
            freq[i] += cnt[unique]
            cnt -= Counter(digits[i] * freq[i])
        return ''.join([str(i) * f for i, f in enumerate(freq)])
