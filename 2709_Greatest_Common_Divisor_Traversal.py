from collections import defaultdict
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        self.index2prime = defaultdict(list)
        self.prime2index = defaultdict(list)
        for i, num in enumerate(nums):
            for d in range(2, int(sqrt(num))+1):
                if num % d == 0:
                    self.index2prime[i].append(d)
                    self.prime2index[d].append(i)
                    while num % d == 0:
                        num //= d
            if num > 1:
                self.index2prime[i].append(num)
                self.prime2index[num].append(i)
        
        visitedIndex = set()
        visitedPrime = set()
        self.dfs(0, visitedIndex, visitedPrime)
        return len(visitedIndex) == len(nums)
        
    def dfs(self, index, visitedIndex, visitedPrime):
        if index in visitedIndex:
            return
        visitedIndex.add(index)
        for prime in self.index2prime[index]:
            if prime in visitedPrime:
                continue
            visitedPrime.add(prime)
            for next in self.prime2index[prime]:
                self.dfs(next, visitedIndex, visitedPrime)
