class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        k_list = []
        while K >= 1:
            k_list.append(K % 10)
            K = K // 10
        if len(A) >= len(k_list):
            big = A[::-1]
            small = k_list
        else:
            big = k_list
            small = A[::-1]
        carry = 0
        for i in range(len(small)):
            big[i] += small[i] + carry
            if big[i] > 9:
                big[i] -= 10
                carry = 1
            else:
                carry = 0
        i = len(small)
        while carry != 0:
            if i == len(big):
                big.append(0)
            big[i] += carry
            if big[i] > 9:
                big[i] -= 10
                carry = 1
            else:
                carry = 0
            i += 1
        return big[::-1]
