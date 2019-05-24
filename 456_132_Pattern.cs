public class Solution {
    public bool Find132pattern(int[] nums) {
        var a3 = Int32.MinValue;
        Stack<int> s = new Stack<int>();
        for (var i = nums.Count() - 1; i >= 0; --i) {
            if (nums[i] < a3) return true;
            while (s.Count() > 0 && nums[i] > s.Peek()) {
                a3 = Math.Max(a3, s.Pop());
            }
            s.Push(nums[i]);
        }
        return false;
    }
}
