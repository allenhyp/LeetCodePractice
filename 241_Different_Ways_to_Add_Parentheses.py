class Solution:
    def worker(self, l, r, s):
        if s == '+':
            return l + r
        elif s == '-':
            return l - r
        else:
            return l * r


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                result += [self.worker(l, r, input[i])
                           for l in left for r in right]
        return result
