from functools import cache
from typing import List

class Solution:
    @cache
    def sprintTotalScore(self, d):
        return (d+1)*d//2
    
    def getMaxPointsFromSprints(self, days: List[int], k: int) -> int:
        totalDays = sum(days)
        if k / totalDays > 2.0:
            return sum([self.sprintTotalScore(ds) for ds in days]) * (k//totalDays-1) + self.getMaxPointsFromSprints(days, totalDays+totalDays%k)
        
        tk, i = k-1, 0
        while tk > 0:
            days.append(min(tk, days[i]))
            tk, i = tk - days[i], i + 1

        n = len(days)
        left_d, left_s, left_index = 0, 0, 0
        ret = cur = 0
        for right_index in range(n):
            right = days[right_index]
            cur += self.sprintTotalScore(right)
            k -= right
            while k < 0 and left_index <= right_index:
                if left_d > 0:
                    k += left_d
                    cur -= left_s
                    left_d = left_s = 0
                    left_index += 1
                else:
                    if -k >= days[left_index]:
                        k += days[left_index]
                        cur -= self.sprintTotalScore(days[left_index])
                        left_index += 1
                    else:
                        left_d = days[left_index] + k
                        left_s = self.sprintTotalScore(days[left_index]) - self.sprintTotalScore(-k)
                        cur -= self.sprintTotalScore(-k)
                        k = 0
            ret = max(ret, cur)
        return ret


s = Solution()
print(s.getMaxPointsFromSprints([2, 3, 2], 15))
# 2,3,2,2,3,2
# 3,6,3,3,6,3