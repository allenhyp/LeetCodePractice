public class Solution {
    public int[] DailyTemperatures(int[] T) {
        Stack<int> s = new Stack<int>();
        int[] res = new int[T.Count()];
        for (int i = T.Count() - 1; i >= 0; --i) {
            while (s.Count() > 0 && T[s.Peek()] <= T[i])
                s.Pop();
            res[i] = s.Count() == 0 ? 0 : s.Peek() - i;
            s.Push(i);
        }
        return res;
    }
}
