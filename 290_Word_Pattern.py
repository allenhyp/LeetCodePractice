class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_arr = str.split(' ')
        dic = {}
        p_len = len(pattern)
        if p_len != len(str_arr):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if str_arr[i] != dic[pattern[i]]:
                    return False
            elif str_arr[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = str_arr[i]
        return True
