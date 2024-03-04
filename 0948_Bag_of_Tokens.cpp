class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int maximum = 0, current = 0;
        sort(tokens.begin(), tokens.end());
        int l = 0, r = tokens.size()-1;
        while (l <= r) {
            if (power >= tokens[l]) {
                current++;
                power -= tokens[l++];
            } else {
                if (current == 0) break;
                current--;
                power += tokens[r--];
            }
            maximum = max(maximum, current);
        }
        return maximum;
    }
};
