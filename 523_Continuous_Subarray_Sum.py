class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = {0: -1}
        subsum = 0
        for i in range(len(nums)):
            subsum = (subsum + nums[i]) % k
            if subsum in visited:
                if i - visited[subsum] > 1:
                    return True
            else:
                visited[subsum] = i
        return False
