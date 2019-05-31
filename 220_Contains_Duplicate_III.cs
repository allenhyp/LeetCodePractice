public class Solution {
    public bool ContainsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k <= 0 || t < 0) return false;
        var buckets = new Dictionary<Int64, Int64>();
        Int64 size = (Int64)t + 1;
        for (int i = 0; i < nums.Count(); ++i) {
            var remappedNum = (nums[i] - Int64.MinValue) / size;
            if (buckets.ContainsKey(remappedNum))
                return true;
            else if (buckets.ContainsKey(remappedNum - 1) && Math.Abs(nums[i] - buckets[remappedNum - 1]) < size)
                return true;
            else if (buckets.ContainsKey(remappedNum + 1) && Math.Abs(nums[i] - buckets[remappedNum + 1]) < size)
                return true;
            if (i >= k) {
                buckets.Remove((nums[i - k] - Int64.MinValue) / size);
            }
            buckets.Add(remappedNum, nums[i]);
        }
        return false;
    }
}
