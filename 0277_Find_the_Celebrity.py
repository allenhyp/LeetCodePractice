# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        if any(knows(candidate, i) for i in range(candidate)):
            return -1
        if any(not knows(i, candidate) for i in range(n)):
            return -1
        return candidate
