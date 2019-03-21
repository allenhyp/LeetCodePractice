class Solution {
private:
    int size;
    vector<string> permutation(string s) {
        vector<string> res;
        size = s.size();
        recursive(s, 0, res);
        return res;
    }

    void recursive(string s, int start, vector<string>& res) {
        if (start == size - 1) res.push_back(s);
        else {
            for (int i = start; i < size; ++i) {
                if (i != start && s[i] == s[start]) continue;
                swap(s[i], s[start]);
                recursive(s, start + 1, res);
            }
        }
    }

public:
    vector<string> generatePalindromes(string s) {
        vector<string> res;
        unordered_map<char, int> count;
        int odd = 0;
        char mid = '!';
        string half;
        if (s.size() <= 1) return vector<string>(1, s);
        for (char c : s) count[c]++;
        for (auto c : count) {
            if (c.second % 2) {
                if (odd == 1) return vector<string> ();
                odd++;
                mid = c.first;
            }
            half += string(c.second / 2, c.first);
        }
        res = permutation(half);
        for (string& r : res) {
            string ori(r);
            reverse(r.begin(), r.end());
            if (odd) r += mid + ori;
            else r += ori;
        }
        return res;
    }
};
