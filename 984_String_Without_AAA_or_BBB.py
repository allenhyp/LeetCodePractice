class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A > B:
            res = ''.join(['ab' for _ in range(B)])
            left = A - B
            c = 'a'
        else:
            res = ''.join(['ba' for _ in range(A)])
            left = B - A
            c = 'b'
        for i in range(left):
            res = res[:i * 3] + c + res[i * 3:]
        return res


class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == 0:
            return 'b' * B
        elif B == 0:
            return 'a' * A
        elif A == B:
            return 'ab' * A
        elif A > B:
            return 'aab' + self.strWithout3a3b(A - 2, B - 1)
        else:
            return self.strWithout3a3b(A - 1, B - 2) + 'abb'
