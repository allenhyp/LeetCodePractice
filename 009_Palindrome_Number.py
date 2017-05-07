class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        head = 0
        tail = len(x) - 1
        while head < tail:
            if x[head] != x[tail]:
                return False
            head = head + 1
            tail = tail - 1
        return True