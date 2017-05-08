class Solution(object):
    def isCommonPrefix(self, targetString, strList):
        for s in strList:
            if not s.startswith(targetString):
                return False
        return True


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        minLenth = len(strs[0])
        minString = ""
        for s in strs:
            if len(s) <= minLenth:
                minString = s
                minLenth = len(s)
        if minString == "":
            return ""
        low = 1
        high = minLenth
        while low <= high:
            medium = (high + low) / 2
            target = minString[0:medium]
            if self.isCommonPrefix(target, strs):
                low = medium + 1
            else:
                high = medium - 1
        return strs[0][0:(high + low) / 2]
