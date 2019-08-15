class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            res[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)
        return res
