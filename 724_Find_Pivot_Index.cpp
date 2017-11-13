#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if (nums.size() < 3) return -1;
        long rightSum = 0, leftSum = 0;
        for (int i = 1; i < nums.size(); i++) {
            rightSum += nums[i];
        }
        for (int i = 0; i < nums.size(); i++) {
            if (leftSum == rightSum) return i;
            leftSum += nums[i];
            rightSum -= nums[i+1];
        }
        return -1;
    }
};

int main(void) {
    vector<int> input = {-1,-1,2};
    Solution mySolution;
    cout << mySolution.pivotIndex(input) << endl;
}
