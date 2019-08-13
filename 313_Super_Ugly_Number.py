class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [float('inf')] * n
        index = [0] * k
        ugly[0] = 1
        for i in range(1, n):
            for j in range(k):
                ugly[i] = min(ugly[i], ugly[index[j]] * primes[j])
            for j in range(k):
                index[j] += 1 if ugly[i] == ugly[index[j]] * primes[j] else 0
        return ugly[-1]
