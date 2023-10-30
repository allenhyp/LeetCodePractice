class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=(lambda x: ("{0:b}".format(x).count('1'), x)))

class Solution:
    def countBits(self, num):
        if num not in self.nbits:
            x = num
            count = 0
            while x > 0:
                count += 1
                x = x & (x - 1)
            self.nbits[num] = count
        return self.nbits[num]
    
    def greater(self, a, b):
        cnta, cntb = self.countBits(a), self.countBits(b)
        if cnta > cntb:
            return 1
        elif cnta == cntb and a > b:
            return 1
        else:
            return -1

    def sortByBits(self, arr: List[int]) -> List[int]:
        self.nbits = {}
        return sorted(arr, key=functools.cmp_to_key(self.greater))
