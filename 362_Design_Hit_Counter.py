class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.appendleft(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.q) and self.q[-1] < timestamp - 299:
            self.q.pop()
        return len(self.q)

        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)