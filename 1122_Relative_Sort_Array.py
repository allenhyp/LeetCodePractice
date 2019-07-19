class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: dic.get(i, 1000 + i))
