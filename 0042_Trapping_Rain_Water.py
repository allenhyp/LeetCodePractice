class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height + [0]
        n = len(height)
        max_left = max_right = 0
        left, right = [0] * n, [0] * n
        for i in range(1, n - 1):
            left[i] = max_left
            max_left = max(max_left, height[i])
        for i in range(n - 2, 0, -1):
            right[i] = max_right
            max_right = max(max_right, height[i])

        ret = 0
        for i in range(n):
            ret += max(0, min(left[i], right[i]) - height[i])
        return ret


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
