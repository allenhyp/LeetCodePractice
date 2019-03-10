class Solution:
    def clumsy(self, N: int) -> int:
        default = [0, 1, 2, 6]
        if (N <= 3):
            return default[N]
        first, temp, sum = True, 0, 0
        while N >= 4:
            temp = N * (N - 1) // (N - 2)
            if first:
                sum = temp + (N - 3)
                first = False
            else:
                sum -= temp - (N - 3)
            N -= 4
        sum -= default[N]
        return sum


class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 2:
            return N
        if N <= 4:
            return N + 3
        if (N - 4) % 4 == 0:
            return N + 1
        elif (N - 4) % 4 <= 2:
            return N + 2
        else:
            return N - 1
