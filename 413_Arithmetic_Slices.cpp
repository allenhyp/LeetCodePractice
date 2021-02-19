class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        if (A.size() < 3) return 0;
        int dp = 0, res = 0;
        for (int i = 2; i < A.size(); ++i) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) ++dp;
            else dp = 0;
            res += dp;
        }
        
        return res;
    }
};
