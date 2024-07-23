class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> counter;
        for (int num : nums) {
            if (counter.find(num) == counter.end()) counter.insert({num, 1});
            else counter[num] += 1;
        }
        vector<pair<int, int>> serial;
        for (auto it = counter.begin(); it != counter.end(); ++it) serial.push_back({it->first, it->second});
        sort(serial.begin(), serial.end(), [&](pair<int, int>& a, pair<int, int>& b){
            if (a.second == b.second) return a.first > b.first;
            return a.second < b.second;
        });
        vector<int> ret;
        for (auto p : serial) ret.insert(ret.end(), p.second, p.first);
        return ret;
    }
};
