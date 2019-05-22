class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.count, self.oldest = 0, 0
        self.window = [0] * size
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.count += 1
        self.sum = self.sum - self.window[self.oldest] + val
        self.window[self.oldest] = val
        self.oldest = (self.oldest + 1) % self.size
        return self.sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
