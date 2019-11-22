class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s, d = [], {}
        for i in range(len(nums2))[::-1]:
            while len(s) and nums2[s[-1]] < nums2[i]:
                s.pop()
            d[nums2[i]] = nums2[s[-1]] if len(s) else -1
            s.append(i)
        return [d[x] for x in nums1]
