class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lh = len(haystack)
        ln = len(needle)
        limit = lh - ln + 1
        if ln == 0:
            return 0
        elif ln > lh:
            return -1
        for i in range(0, limit):
            j = 0
            while j < ln:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == ln:
                return i
        return -1
