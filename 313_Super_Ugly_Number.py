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


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, q = [1], []
        for prime in primes:
            heapq.heappush(q, (prime, 0, prime))
            
        for _ in range(1, n):
            min_v, index, prime = q[0]
            dp.append(min_v)
            while q[0][0] == min_v:
                min_v, index, prime = heapq.heappop(q)
                heapq.heappush(q, (prime * dp[index + 1], index + 1, prime))
        return dp[-1]
