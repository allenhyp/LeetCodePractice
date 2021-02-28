public class Solution {
    public int Trap(int[] height) {
        int sum = 0;
        Stack<int> s = new Stack<int> ();
        for (int i = 0; i < height.Count(); ++i) {
            while (s.Count() > 0 && height[i] > height[s.Peek()]) {
                int top = s.Pop();
                if (s.Count() == 0) break;
                int d = i - s.Peek() - 1;
                int h = Math.Min(height[i], height[s.Peek()]) - height[top];
                sum += d * h;
            }
            s.Push(i);
        }
        return sum;
    }
}
