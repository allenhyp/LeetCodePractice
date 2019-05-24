public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        var dic = new Dictionary<int, int>();
        var s = new Stack<int>();
        foreach (var num in nums2) {
            while (s.Count() > 0 && s.Peek() < num) {
                dic[s.Pop()] = num;
            }
            s.Push(num);
        }
        for (var i = 0; i < nums1.Count(); ++i) {
            nums1[i] = dic.ContainsKey(nums1[i]) ? dic[nums1[i]] : -1;
        }
        return nums1;
    }
}
