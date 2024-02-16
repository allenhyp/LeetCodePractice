bool cmpValue(pair<int, int> a, pair<int, int> b) {
    return a.second < b.second;
}

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        map<int, int> counter;
        for (int num : arr) counter[num]++;
        vector<pair<int, int>> vc;
        for (auto c : counter) vc.push_back({c.first, c.second});
        sort(vc.begin(), vc.end(), cmpValue);
        int remove = 0;
        auto it = vc.begin();
        while (it != vc.end() && k >= it->second) {
            remove++;
            k -= it++->second;
        }
        return vc.size() - remove;
    }
};
