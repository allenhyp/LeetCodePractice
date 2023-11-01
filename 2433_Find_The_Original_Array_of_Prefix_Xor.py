'''
a ^ b = c
a ^ a ^ b = a ^ c
0 ^ b = a ^ c
b = a ^ c
'''

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret = [pref[0]]
        for i in range(1, len(pref)):
            ret.append(pref[i - 1] ^ pref[i])
        return ret
