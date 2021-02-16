class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [""]
        def addChar(c):
            nr = []
            for r in res:
                nr.append(r + c)
            return nr
        
        for c in S:
            if c.isdigit():
                res = addChar(c)
            else:
                res = addChar(c.lower()) + addChar(c.upper())
        return res
