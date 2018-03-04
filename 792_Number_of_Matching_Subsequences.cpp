class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        vector<vector<int> > alpha(26);
        int result = 0;
        for (int i = 0; i < S.size(); i++)
            alpha[S[i] - 'a'].push_back(i);
        for (auto word : words) {
            bool found = true;
            int index = -1;
            for (auto c : word) {
                auto it = upper_bound(alpha[c - 'a'].begin(), alpha[c - 'a'].end(), index);
                if (it >= alpha[c-'a'].end()) found = false;
                else index = *it;
            }
            if (found) result++;
        }
        return result;
    }
};
