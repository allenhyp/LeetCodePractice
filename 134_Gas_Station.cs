public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, subsum = Int32.MaxValue, start = 0;
        for (int i = 0; i < gas.Length; ++i) {
            total += gas[i] - cost[i];
            if (total < subsum) {
                start = i + 1;
                subsum = total;
            }
        }
        return total >= 0 ? start % gas.Length : -1;
    }
}
