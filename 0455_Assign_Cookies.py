class Solution:
    def findContentChildren(self, greeds: List[int], sizes: List[int]) -> int:
        greeds.sort()
        sizes.sort()
        index = 0
        ret = 0
        for g in greeds:
            while index < len(sizes) and sizes[index] < g:
                index += 1
            if index == len(sizes):
                break
            ret, index = ret + 1, index + 1
        return ret
