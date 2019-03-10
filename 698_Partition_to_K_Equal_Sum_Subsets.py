class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        self.n = len(nums)
        if k > self.n:
            return False
        self.total = sum(nums)
        if self.total % k:
            return False
        self.target = self.total // k
        self.visited = [False] * self.n
        nums.sort(reverse=True)
        def dfs(k, index, sum):
            if k == 0:
                return True
            if sum == self.target:
                return dfs(k - 1, 0, 0)
            for i in range(index, self.n):
                if not self.visited[i] and sum + nums[i] <= self.target:
                    self.visited[i] = True
                    if dfs(k, i + 1, sum + nums[i]):
                        return True
                    self.visited[i] = False
            return False
        return dfs(k, 0, 0)
