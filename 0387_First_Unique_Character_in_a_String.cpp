class Solution {
public:
    int firstUniqChar(string s) {
        // For large string: traverse string once and the map once.
        unordered_map<char, pair<int, int>> m;
        int idx = s.size();
        for (int i = 0; i < idx; i++) {
            m[s[i]].first++;
            m[s[i]].second = i; 
        }
        for (auto &p: m) {
            if (p.second.first == 1) idx = min(idx, p.second.second);
        }
        return idx == s.size() ? -1 : idx;
    }

    int firstUniqChar(string s) {
        // For small string: traverse string twice.
        unordered_map<char, int> m;
        for (auto &c: s) {
            m[c]++;
        }
        for (int i=0; i < s.size(); i++) {
            if (m[s[i]] == 1) return i;
        }
        return -1;
    }
};
