class MinStack:
    class Node:
        def __init__(self, val, minimum, next=None):
            self.val = val
            self.minimum = minimum
            self.next = next
        
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head == None:
            self.head = self.Node(x, x)
        else:
            self.head = self.Node(x, min(self.head.minimum, x), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        return self.head.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
