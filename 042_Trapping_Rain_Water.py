class Solution:
    def trap(self, height: List[int]) -> int:
        stack, res = [], 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                d = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                res += d * h
            stack.append(i)
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, left_max, right_max, res = 0, len(height) - 1, 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    res += max(left_max - height[left], 0)
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    res += max(right_max - height[right], 0)
                right -= 1
        return res
