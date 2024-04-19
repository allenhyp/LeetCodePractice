class Solution:

    def __init__(self, w: List[int]):
        self.acc = [w[0]]
        for i in range(1, len(w)):
            self.acc.append(w[i]+self.acc[-1])

    def pickIndex(self) -> int:
        rn = random.randint(1, self.acc[-1])
        return bisect.bisect_left(self.acc, rn)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
