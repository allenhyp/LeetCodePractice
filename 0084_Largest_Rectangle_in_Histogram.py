class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        less_from_left = [-1] * n
        less_from_right = [n] * n
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p
        
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (less_from_right[i] - less_from_left[i] - 1))
        
        return max_area


# monostack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                # We need to extract some stuffs from our stack,
                # until it becomes increasing one.
                h = heights[stack.pop()]
                w = (i - 1 - stack[-1]) if stack else i
                maxArea = max(maxArea, h * w)
            stack.append(i)
        return maxArea
