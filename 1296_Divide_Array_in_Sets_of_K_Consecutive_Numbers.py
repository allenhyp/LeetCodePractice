from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        counter = Counter(nums)
        keys = sorted(counter.keys())
        
        for key in keys:
            if counter[key] > 0:
                cnt = counter[key]
                for i in range(k):
                    if counter[key + i] - cnt >= 0:
                        counter[key + i] -= cnt
                    else:
                        return False
        return True
