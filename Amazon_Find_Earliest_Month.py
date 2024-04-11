from typing import List
class Solution:
    def findEarliestMonth(self, stockPrice: List[int]) -> int:
        acc = [stockPrice[0]]
        for sp in stockPrice[1:]:
            acc.append(acc[-1]+sp)

        n = len(stockPrice)
        minimum_price_change = float('inf')
        ret = -1
        for i in range(1, n):
            pre = acc[i]
            post = acc[-1] - pre
            price_change = abs(pre//(i) - post//(n-i))
            if price_change < minimum_price_change:
                minimum_price_change = price_change
                ret = i

        return ret

    
s = Solution()
# stockPrice = [1, 3, 2, 3]
stockPrice = [1, 3, 2, 4, 5]
print(s.findEarliestMonth(stockPrice))
