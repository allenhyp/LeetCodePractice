class Solution {
private:
    int helper(vector<int>& p, int start) {
        if (start == 0) return 1;
        int cnt = 0;
        for (int i = start; i > 0; --i) {
            swap(p[i], p[start]);
            if (start % p[start] == 0 || p[start] % start == 0)
                cnt += helper(p, start - 1);
            swap(p[i], p[start]);
        }
        return cnt;
    }
public:
    int countArrangement(int n) {
        vector<int> p (n + 1);
        for (int i = 0; i < n + 1; ++i) p[i] = i;
        return helper(p, n);
    }
};
