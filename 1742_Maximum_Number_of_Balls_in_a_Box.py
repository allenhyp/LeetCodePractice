class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 46
        for i in range(lowLimit, highLimit + 1):
            box[sum([int(d) for d in str(i)])] += 1
        return max(box)
