class Solution:
    def largestGoodInteger(self, num: str) -> str:
        check = 999
        while check > 0:
            if str(check) in num:
                return str(check)
            check -= 111
        return "000" if "000" in num else ""
