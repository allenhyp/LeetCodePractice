class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, idx, n = [], 0, len(pushed)
        for target in popped:
            while (len(stack) == 0 or stack[-1] != target) and idx < n:
                stack.append(pushed[idx])
                idx += 1
            if stack[-1] != target:
                return False
            stack.pop()
        return True
