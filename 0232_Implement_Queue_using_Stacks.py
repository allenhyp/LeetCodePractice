class MyQueue:

    def __init__(self):
        self.inward = []
        self.outward = []

    def push(self, x: int) -> None:
        self.inward.append(x)

    def pop(self) -> int:
        if not self.outward:
            self.transfer()
        return self.outward.pop()

    def peek(self) -> int:
        if not self.outward:
            self.transfer()
        return self.outward[-1]

    def empty(self) -> bool:
        return len(self.inward) == 0 and len(self.outward) == 0

    def transfer(self):
        while self.inward:
            self.outward.append(self.inward.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()