class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ret = money - prices[0] - prices[1]
        return ret if ret >= 0 else money
