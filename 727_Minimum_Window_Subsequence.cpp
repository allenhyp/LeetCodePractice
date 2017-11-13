/*
For substring S[0, i] and T[0, j], 
dp[i][j] is starting index k of the shortest postfix of S[0, i], such that T[0, j] is a subsequence of S[k, i]. 
Here T[0] = S[k], T[j] = S[i]. Otherwise, dp[i][j] = -1.

The goal is the substring with length of min(i-dp[i][n-1]) for all i < m,  where m is S.size() and n is T.size() 
Initial condition: dp[i][0] = i if S[i] = T[0], else -1
Equations: If S[i] = T[j], dp[i][j] = max(dp[k][j-1]) for all k < i; else dp[i][j] = -1;
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string minWindow(string S, string T) {
        int m = S.size(), n = T.size();
        vector<vector<int> > dp(n, vector<int>(m, -1));
        for (int i = 0; i < m; i++) {
            if (S[i] == T[0])
                dp[0][i] = i;
        }
        for (int j = 1; j < n; j++) {
            int k = -1;
            for (int i = 0; i < m; i++) {
                if (k != -1 && S[i] == T[j]) dp[j][i] = k;
                if (dp[j-1][i] != -1) k = dp[j-1][i];
            }
        }
        int st = -1, len = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (dp[n-1][i] != -1 && i - dp[n-1][i] + 1 < len) {
                st = dp[n-1][i];
                len = i - dp[n-1][i] + 1;
            }
        }
        return st == -1 ? "" : S.substr(st, len);
    }
};

int main(void) {
    string s = "fgrqsqsnodwmxzkzxwqegkndaa";
    string t = "fnok";
    Solution mySolution;
    cout << mySolution.minWindow(s, t) << endl;
    return 0;
}
