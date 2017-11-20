class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        result = {0: [[]], 1: [[s[0]]]}
        for i in range(1, n):
            result[i + 1] = []
            for j in range(0, i + 1):
                if self.isPal(s[j : i + 1]):
                    for prev in result[j]:
                        result[i + 1].append(prev + [s[j : i + 1]])
        return result[n]


    def isPal(self, string):
        return string == string[::-1]
