class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        bool inserted = false;
        for (auto interval : intervals) {
            if (interval[1] < newInterval[0]) res.push_back(interval);
            else if (interval[0] > newInterval[1]) {
                if (!inserted) {
                    res.push_back(newInterval);
                    inserted = true;
                }
                res.push_back(interval);
            } else {
                newInterval[0] = min(newInterval[0], interval[0]);
                newInterval[1] = max(newInterval[1], interval[1]);
            }
        }
        if (!inserted) res.push_back(newInterval);
        return res;
    }
};