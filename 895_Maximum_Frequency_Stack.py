class FreqStack:

    def __init__(self):
        self.freqMap = collections.defaultdict(int)
        self.stackMap = collections.defaultdict(list)
        self.maxFreq = 0

    def push(self, x: int) -> None:
        self.freqMap[x] += 1
        self.maxFreq = max(self.maxFreq, self.freqMap[x])
        self.stackMap[self.freqMap[x]].append(x)
        
    def pop(self) -> int:
        res = self.stackMap[self.maxFreq].pop()
        if len(self.stackMap[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.freqMap[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
