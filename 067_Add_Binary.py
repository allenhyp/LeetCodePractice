class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        res = ''
        while m >= 0 or n >= 0 or carry > 0:
            if m >= 0:
                if a[m] == '1':
                    carry += 1
                m -= 1
            if n >= 0:
                if b[n] == '1':
                    carry += 1
                n -= 1
            res = str(carry % 2) + res
            carry = carry // 2
        return res
