class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int iter = 0, line = 1, w;
        for (int i = 0; i < S.size(); i++) {
            w = widths[S[i] - 'a'];
            if (iter + w > 100) {
                iter = w;
                line++;
            }
            else 
                iter += w;
        }
        if (line == 1 && iter == 0) line = 0;
        vector<int> result = {line, iter};
        return result;
    }
};
