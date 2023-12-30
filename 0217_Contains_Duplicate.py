class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for num in nums:
            if num not in record:
                record.add(num)
            else:
                return True
        return False
