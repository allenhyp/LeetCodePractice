class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1: return n
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy[i - 1] = max(candy[i - 1], candy[i] + 1)
        return sum(candy)


# Use two variables 'up' and 'down' to count the steps of continuous up and down respectively, 
# and a 'peak' representing the peak before going down. (One pass, O(1) space)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1: return n
        up = down = peak = 0
        res = 1
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                up += 1
                peak, down = up, 0
                res += 1 + up
            elif ratings[i - 1] == ratings[i]:
                up = down = peak = 0
                res += 1
            else:
                up = 0
                down += 1
                res += 1 + down + (0 if peak < down else -1)
        return res

