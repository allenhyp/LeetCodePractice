#include <iostream>
#include <vector>
#include "stdio.h"
using namespace std;

class Solution {
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target) {
        vector<vector<int> > res;
        int len = nums.size();
        if (len < 4) return res;
        sort(nums.begin(), nums.end());
        for (int i=0; i<len-3; i++) {
            if (i>0 && nums[i] == nums[i-1]) continue;
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;
            if (nums[i] + nums[len-3] + nums[len-2] + nums[len-1] < target) continue;
            for (int j=i+1; j<len-2; j++) {
                if (j>i+1 && nums[j]==nums[j-1]) continue;
                if (nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
                if (nums[i] + nums[j] + nums[len-2] + nums[len-1] < target) continue;
                int lower = j+1, upper = len-1;
                while (lower < upper) {
                    int sum = nums[i] + nums[j] + nums[lower] + nums[upper];
                    if (sum < target) lower++;
                    else if (sum > target) upper--;
                    else {
                        res.push_back(vector<int>{nums[i], nums[j], nums[lower], nums[upper]});
                        printf("[%d,%d,%d,%d]\n", nums[i], nums[j], nums[lower], nums[upper]);
                        do {lower++;} while (nums[lower]==nums[lower-1] && lower<upper);
                        do {upper--;} while (nums[upper]==nums[upper+1] && lower<upper);
                    }
                }
            }
        }
        return res;
    }
};

int main(void) {
    Solution mySolution;
    vector<int> input = vector<int>{1,0,-1,0,-2,2};
    int target = 0;
    vector<vector<int> > output = mySolution.fourSum(input, target);
    return 0;
}
