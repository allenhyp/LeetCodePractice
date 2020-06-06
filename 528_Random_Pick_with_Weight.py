class Solution:

    def __init__(self, w: List[int]):
        self.list = [w[0]]
        for i in range(1, len(w)):
            self.list.append(self.list[-1] + w[i])
        self.n = len(self.list)

    def pickIndex(self) -> int:
        target = randrange(self.list[-1])
        left, right = 0, self.n - 1
        while left < right:
            mid = (left + right) // 2
            if self.list[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
