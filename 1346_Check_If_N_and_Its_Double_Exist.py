class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        met = set()
        for a in arr:
            if a / 2 in met or a * 2 in met:
                return True
            met.add(a)
        return False
