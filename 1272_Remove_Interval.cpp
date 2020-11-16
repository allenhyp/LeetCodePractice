class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals, vector<int>& toBeRemoved) {
        vector<vector<int>> res;
        for (auto itv : intervals) {
            if (itv[1] <= toBeRemoved[0] || itv[0] >= toBeRemoved[1]) res.push_back(itv);
            else {
                if (itv[0] < toBeRemoved[0]) res.push_back({itv[0], toBeRemoved[0]});
                if (itv[1] > toBeRemoved[1]) res.push_back({toBeRemoved[1], itv[1]});
            }
        }
        
        return res;
    }
};
