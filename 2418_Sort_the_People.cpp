class Solution {
public:
    bool pairSortByHeight(pair<string, int>& a, pair<string, int>& b) {
        return a.second > b.second;
    }

    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<string, int>> pairs;
        vector<string> ret;
        for (int i = 0; i < names.size(); ++i) {
            pairs.push_back({names[i], heights[i]});
        }
        sort(pairs.begin(), pairs.end(), [this](pair<string, int>& a, pair<string, int>& b){return this->pairSortByHeight(a, b);});
        for (auto p : pairs) {
            ret.push_back(p.first);
        }
        return ret;
    }
};
