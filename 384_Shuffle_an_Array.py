class Solution:

    def __init__(self, nums: List[int]):
        self.raw = nums[:]
        self.arr = nums[:]
        self.size = len(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.raw
    

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(self.size):
            r = random.randint(0, self.size - 1)
            self.arr[i], self.arr[r] = self.arr[r], self.arr[i]
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
