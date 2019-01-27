class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = {}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key in self.queue:
            heapq.heappush(self.queue[key], (-timestamp, value))
        else:
            self.queue[key] = [(-timestamp, value)]

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key in self.queue:
            for t, v in self.queue[key]:
                if -t <= timestamp:
                    return v
        return ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
