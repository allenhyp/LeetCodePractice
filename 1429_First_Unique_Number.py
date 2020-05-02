class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.dic = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.queue):
            if self.dic[self.queue[-1]] == 1:
                return self.queue[-1]
            else:
                self.queue.pop()
        return -1

    def add(self, value: int) -> None:
        if value not in self.dic:
            self.queue.appendleft(value)
        self.dic[value] = self.dic.get(value, 0) + 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
