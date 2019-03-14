class Solution {
private:
    vector<int> c;

public:
    Solution(vector<int> w) {
        for (int i : w) c.push_back(c.empty() ? i : i + c.back());
    }
    
    int pickIndex() {
        int target = rand() % c.back();
        int l = 0, h = c.size() - 1;
        while (l < h) {
            int m = (l + h) / 2;
            if (target < c[m]) h = m;
            else l = m + 1;
        }
        return l;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
