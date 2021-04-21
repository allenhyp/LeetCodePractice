public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        for (int i = 1; i < triangle.Count; ++i) {
            triangle[i][0] += triangle[i - 1][0];
            for (int j = 1; j < i; ++j) {
                triangle[i][j] += Math.Min(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
            triangle[i][i] += triangle[i - 1][i - 1];
        }
        
        int res = Int32.MaxValue;
        foreach (var path in triangle[triangle.Count - 1]) {
            res = Math.Min(res, path);
        }
        
        return res;
    }
}
