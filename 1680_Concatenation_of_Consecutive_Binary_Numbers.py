class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join(bin(i).replace("0b", "") for i in range(1, n + 1)), 2) % (10 ** 9 + 7)
