class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> dic;
        int start = 0, maxLen = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (dic.find(s[i]) != dic.end())
                start = max(start, dic[s[i]] + 1);
            maxLen = max(maxLen, i - start + 1);
            dic[s[i]] = i;
        }
        return maxLen;
    }
};
