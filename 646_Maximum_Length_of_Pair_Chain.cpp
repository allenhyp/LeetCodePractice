#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int count = 0;
        sort(pairs.begin(), pairs.end(), cmp);
        vector<int>& pair = pairs[0];
        for (int i = 0; i < pairs.size(); ++i) {
            if (i == 0 || pair[1] < pairs[i][0]) {
                pair = pairs[i];
                count++;
            }
        }
        return count;
    }
    static bool cmp(vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    }
};

