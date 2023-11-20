from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.map[key][0][1]:
            return ""
        arr = self.map[key]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if arr[mid][1] > timestamp:
                right = mid
            else:
                left = mid + 1
        return arr[left - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)