class Solution:
    def nChoose2(self, n):
        return n * (n - 1) // 2
    def countHomogenous(self, s: str) -> int:
        cont, total = 1, 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                total = (total + self.nChoose2(cont + 1)) % (10**9 + 7)
                cont = 1
            else:
                cont += 1
        return (total + self.nChoose2(cont + 1)) % (10**9 + 7)
