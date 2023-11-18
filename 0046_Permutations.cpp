class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > result;
        permuteRecursive(result, 0, nums);
        return result;
    }
    
    void permuteRecursive(vector<vector<int> >& r, int begin, vector<int>& n) {
        if (begin >= n.size()) {
            r.push_back(n);
            return;
        }
        for (int i = begin; i < n.size(); i++) {
            swap(n[begin], n[i]);
            permuteRecursive(r, begin+1, n);
            swap(n[begin], n[i]);
        }
    }
};

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > result;
        vector<int> temp;
        vector<bool> used (nums.size(), false);
        sort(nums.begin(), nums.end());
        permuteRecursive(result, temp, nums, used);
        return result;
    }

    void permuteRecursive(vector<vector<int> >& r, vector<int>& t, vector<int>& n, vector<bool>& u) {
        if (t.size() >= n.size()) {
            r.push_back(t);
            return;
        }
        for (int i = 0; i < n.size(); i++) {
            if (i > 0 && n[i] == n[i-1] && !u[i - 1]) continue;
            t.push_back(n[i]);
            u[i] = true;
            permuteRecursive(r, t, n);
            t.pop_back();
            u[i] = false;
        }
    }
};
