# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.bq = collections.deque()
    
    def read(self, buf: List[str], n: int) -> int:
        index = 0
        while index < n:
            if self.bq:
                buf[index] = self.bq.pop()
                index += 1
            else:
                temp = [''] * 4
                size = read4(temp)
                if size == 0:
                    break
                for i in range(size):
                    self.bq.appendleft(temp[i])

        return index
