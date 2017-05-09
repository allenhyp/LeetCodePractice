class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3}
        stack = []
        head = 0
        for p in s[::1]:
            i = d[p]
            if i > 0:
                stack.append(i)
            else:
                if len(stack) != 0:
                    if stack.pop() + i != 0:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
