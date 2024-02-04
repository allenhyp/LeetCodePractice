class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> targets;
        for (auto c : t) targets[c]++;

        int count = 0;
        int low = 0;
        int min_length = INT_MAX, min_start = 0;
        for (int high = 0; high < s.size(); high++) {
            if (targets[s[high]] > 0) count++;
            targets[s[high]]--;
            if (count == t.size()) {
                while (low < high && targets[s[low]] < 0) {
                    targets[s[low++]]++;
                }
                if (high - low + 1 < min_length) {
                    min_length = high - low + 1;
                    min_start = low;
                }
            }
        }
        return min_length == INT_MAX ? "" : s.substr(min_start, min_length);
    }
};
