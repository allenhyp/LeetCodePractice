class TweetCounts:

    def __init__(self):
        self.dic = collections.defaultdict(list)
        self.delta = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.dic[tweetName], time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        d = self.delta[freq]
        times = self.dic[tweetName]
        left, right = bisect.bisect_left(times, startTime), bisect.bisect_left(times, endTime + 1)
        res = [0] * ((endTime - startTime) // d + 1)
        for i in range(left, right):
            res[(times[i] - startTime) // d] += 1
        return res
        

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
