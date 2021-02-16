class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int, int>> rows;
        vector<int> res;
        int m = mat.size(), n = mat[0].size();
        for (int i = 0; i < m; ++i) {
            int left = 0, right = n - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (mat[i][mid] == 1) left = mid + 1;
                else right = mid - 1;
            }
            cout << left << endl;
            rows.push_back({left, i});
        }
        sort(rows.begin(), rows.end());
        for (int i = 0; i < k; ++i) {
            res.push_back(rows[i].second);
        }
        return res;
    }
};
