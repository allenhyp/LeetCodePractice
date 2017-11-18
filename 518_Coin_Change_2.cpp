#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int> > dp(coins.size() + 1, vector<int> (amount + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= coins.size(); i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= amount; j++) {
                dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j - coins[i-1]] : 0);
            }
        }
        return dp[coins.size()][amount];
    }
};

int main(void) {
    Solution mySolution;
    vector<int> coins = {5,2,4};
    int amount = 10;
    cout << mySolution.change(amount, coins) << endl;
    return 0;
}
