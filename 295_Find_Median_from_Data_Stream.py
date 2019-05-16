class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bigger = []
        self.smaller = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bigger, num)
        heapq.heappush(self.smaller, -heapq.heappop(self.bigger))
        if len(self.bigger) < len(self.smaller):
            heapq.heappush(self.bigger, -heapq.heappop(self.smaller))
    def findMedian(self) -> float:
        if len(self.bigger) > len(self.smaller):
            return self.bigger[0]
        else:
            return (self.bigger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
