class Solution:
    def decodeString(self, s: str) -> str:
        cnt, stk = [], []
        cur = ''
        idx, n = 0, len(s)
        while idx < n:
            if s[idx].isdigit():
                count = 0
                while idx < n and s[idx].isdigit():
                    count = count * 10 + ord(s[idx]) - ord('0')
                    idx += 1
                cnt.append(count)
                idx -= 1
            elif s[idx] == '[':
                stk.append(cur)
                cur = ''
            elif s[idx] == ']':
                cur = stk.pop() + cnt.pop() * cur
            else:
                cur += s[idx]
            idx += 1
        return cur
